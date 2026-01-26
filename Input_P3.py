import tkinter as tk
from tkinter import messagebox
import os, argparse

def Input_2D(Spec_dirc,P3_dirc):
    text = f"""Format = Pipe

# define the Spectrum path
Spec_dirc = {Spec_dirc}

# path to save the P3 processed spectrum
P3_dirc = {P3_dirc}

# define the network path
Dirc_2D = Path_to_Trained/Probability_2D/US

# delation along indirect dimention (by defult it is 1)
Skip_0 = 1

# thereshold (It is used for 2D)
Spe_The = 0.5

# Peak List params
# produce P5 peak list?
PL = YES
# probability thereshould 
PL_The = 0.2
# PN - use Pos and Neg  peaks 
PN_Peak = P

#By default is None BUT change if the spectrum does not have standard name such as: N15HSQC, HMQC, HNCO, HNCA, HNcoCA, HNcaCO, CBCANH, CBCAcoNH
Spec_type = None
"""
    return text

def Input_3D(Spec_dirc,P3_dirc):
    text = f"""Format = Pipe

# define the Spectrum path
Spec_dirc = {Spec_dirc}

# path to save the P3 processed spectrum
P3_dirc = {P3_dirc}

# define the network path
Dirc_2D = Path_to_Trained/Probability_2D/PR
Dirc_3D = Path_to_Trained/Probability_3D

# delation along indirect dimention (by defult it is 1)
Skip_0 = 1
Skip_1 = 1 

# define the Support path. For without support NO. 
Support_dirc = NO
# projected axis in the 3D support spectrum  0,1,2 - Z, Y, X (N,C,H). For 2D HSQC use 1
Support_axis = 1
# Thereshould in the P3 of the support spectrum. THis is used as a mask for for RoI 
Support_The = 0.25

# thereshold for ROI from multiplication of the projections
Fil_The = 0.000625

# noise thereshould factor for P3
# comment out for auto, which is the default 
# 0 - for spectra with only positive relevant peaks
# for pos&neg peaks the fraction of data threshould (e.g. 0.01) in 3D to avoid cancelations of peaks in the projection
PN_The = 0.0

# Produce P3 projections?
Proj = YES

# Peak List params
# produce P5 peak list?
PL = YES
# probability thereshould 
PL_The = 0.1
# PN - use Pos and Neg  peaks 
PN_Peak = P

#By default is None BUT change if the spectrum does not have standard name such as: N15HSQC, HMQC, HNCO, HNCA, HNcoCA, HNcaCO, CBCANH, CBCAcoNH
Spec_type = None
"""
    return text

def main(Spec_dirc,Spec_Dim,Output=None):
    P3_dirc = os.path.splitext(Spec_dirc)[0] + ".P3"
    if Output is None: Output = os.path.join(os.path.dirname(os.path.abspath(__file__)),f"{os.path.splitext(os.path.basename(Spec_dirc))[0]}.input")
    # Create file if not exists
    if not os.path.exists(Output):
        with open(Output, "w", encoding="utf-8") as f:
            if Spec_Dim == 2: f.write(Input_2D(Spec_dirc,P3_dirc))
            if Spec_Dim == 3: f.write(Input_3D(Spec_dirc,P3_dirc))

    # GUI
    root = tk.Tk()
    root.title("Edit Configuration File")
    root.geometry("800x600")

    text = tk.Text(root, wrap="word", font=("Courier", 10))
    text.pack(expand=True, fill="both")

    # Load content
    with open(Output, "r", encoding="utf-8") as f: text.insert("1.0", f.read())

    def save_file():
        with open(Output, "w", encoding="utf-8") as f: f.write(text.get("1.0", "end-1c"))
        messagebox.showinfo("Saved", f"{os.getcwd()}/{Output} saved successfully")
        root.destroy()

    save_btn = tk.Button(root, text="Save", command=save_file)
    save_btn.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Generate Input parameter file for P3.")
    ap.add_argument("-spec", required=True, help="Path to spectrum file (Pipe or Bruker pdata).")
    ap.add_argument("-dim", required=True, help="Spectrum dimention (2 or 3).", type=int)
    ap.add_argument("-o", default=None, help="Output file path (optional).")
    args = ap.parse_args()
    main(args.spec, args.dim, args.o)