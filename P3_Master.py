import os, argparse, subprocess, sys
import nmrglue as ng
import numpy as np
Path = '/home/nmrbox/0016/ajahangiri/Documents/Article_4/MRAi'; sys.path.append(os.path.abspath(Path))
import MRAi_P3 as P3
#####################################################################
def parse_input_file(filename):
    params = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                key, value = [x.strip() for x in line.split('=', 1)]
                params[key] = value
    return params
#####################################################################
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('inputs', nargs='+', help='input file(s)')
    args = parser.parse_args()
    
    for input_file in args.inputs:
        params = parse_input_file(input_file)
        Format = params.get('Format', 'Pipe')
        S_dirc = params.get('Spec_dirc')
        if Format != 'Pipe':
            print("Input file should be in pipe format.")
            sys.exit(1)
        elif not os.path.isfile(S_dirc):
            print("Input file is not available.")
            sys.exit(1)
        else:
            dic, S = ng.pipe.read(S_dirc)

        if S.ndim == 2:
            Dirc_2D = params.get('Dirc_2D')
            Spe_The = float(params.get('Spe_The', 0.5))
            Skip = [int(params.get('Skip_0', 1)),1]
            P = P3.StoP3.P3_2D(S, Dirc_2D, Skip,Spe_The)      

        if S.ndim == 3:
            Dirc_3D = params.get('Dirc_3D')
            Dirc_2D = params.get('Dirc_2D')
            Skip = [int(params.get('Skip_0', 1)),int(params.get('Skip_1', 1)),1]
            Support_dirc = params.get('Support_dirc', 'NO')
            Support_axis = int(params.get('Support_axis', 0))
            Support_The = float(params.get('Support_The', 0.25))
            Fil_The = float(params.get('Fil_The', 0.025**3))
            PN_The = float(params.get('PN_The', 0))
            Slice_Size = int(params.get('Slice_Size', 256))
            if Support_dirc == 'NO': Support = np.zeros((1,))
            if Support_dirc != 'NO': _ , Support = ng.pipe.read(Support_dirc)
            P = P3.StoP3.P3_3D(S,Dirc_3D,Dirc_2D,Skip,Support,Support_axis,Support_The,Fil_The,PN_The,Slice_Size) 
        
        P_dirc = params.get('P3_dirc')
        ng.pipe.write(P_dirc,dic,np.float32(P),overwrite='True')

        if params.get('PL', 'YES') == 'YES':
            PL_The = float(params.get('PL_The', 0.2))
            PN_Peak = params.get('PN_Peak','P')
            P5_dirc = os.path.splitext(S_dirc)[0] + '.P5'
            P3.P3toP5.main(P_dirc,S_dirc,PN_Peak,PL_The,Format,out=P5_dirc)
            Peaks_dirc = os.path.splitext(S_dirc)[0] + '.peaks'
            Spec_type = params.get('Spec_type','None')              
            P3.P5toPeaks.main(P5_dirc,S_dirc,Spec_type,Peaks_dirc)
            Tab_dirc = os.path.splitext(S_dirc)[0] + '.tab'
            P3.PeakstoTab.main(Peaks_dirc,S_dirc,Tab_dirc)
        
        if (params.get('Proj','NO')=='YES') and (S.ndim == 3):
            subprocess.run(["./3Dto2Dproj.sh", S_dirc])
            subprocess.run(["./3Dto2Dproj.sh", P_dirc])
            if params.get('PL', 'YES') == 'YES': P3.Tab3Dto2Dproj.main(Tab_dirc)
        

