def format_coeff(c):
    """Formats coefficient to display a clean + or - sign"""
    try:
        c_val = complex(c)
    except ValueError:
        return str(c)

    # make -- into + etc
    if c_val.imag != 0:
        if c_val.imag >= 0:
            return f"+{c_val.imag}i"
        else:
            return f"{c_val.imag}i"  # negative sign included
    else:
        return f"+{int(c_val.real)}" if c_val.real >= 0 else f"{int(c_val.real)}"

def teleportation_decomposition(alpha, beta):
    α, β = alpha, beta

    print("\n Quantum Teleportation")
    print(f"|psi⟩ₐ = {format_coeff(α)}|0⟩ {format_coeff(β)}|1⟩")

    print("\nThe total state expands as:")
    print("1/(2√2) [")
    print(f"  |phi_I⟩ ⊗ ({format_coeff(α)}|0⟩ {format_coeff(β)}|1⟩)")
    print(f"+ |phi_Z⟩ ⊗ ({format_coeff(α)}|0⟩ {format_coeff(β)}|1⟩)")
    print(f"+ |phi_X⟩ ⊗ ({format_coeff(β)}|0⟩ {format_coeff(α)}|1⟩)")
    print(f"+ |phi_Y⟩ ⊗ ({format_coeff(β)}|0⟩ {format_coeff(α)}|1⟩)")
    print("]\n")

    print("Measurement results and required operations:")
    print("λ₁ → do nothing (I)")
    print("λ₂ → apply Z")
    print("λ₃ → apply X")
    print("λ₄ → apply Y")


if __name__ == "__main__":
    print("\n Teleportation Formula Generator (Clean Signs)")
    alpha = input("Enter α (e.g., 1, -1, i, -i): ")
    beta = input("Enter β (e.g., 1, -1, i, -i): ")
    teleportation_decomposition(alpha, beta)
