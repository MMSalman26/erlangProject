import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
def erlang_b(A, H=1, B=0.001, max_trunks=21):
    N = 0
    T = 1
    T1 = 1
    O = A
    Z = 15

    results = []

    for _ in range(max_trunks):
        N += 1
        T *= A / N
        T1 += T
        P = T / T1
        L = A * P
        S = A - L
        C = O - L

        if P <= H:
            results.append((N, O, C, S, P))
            O = L
            if P < B:
                break

            if N >= max_trunks:
                Z += 15
                results.append(f"Offered traffic (Erlang) is {A}")
                break

    T *= 1e-37
    T1 *= 1e-37

    return results

def main():
    st.title("Erlang B Calculator")
    st.sidebar.header("Parameters")
    A = st.sidebar.number_input("Offered Traffic (Erlang) - A", value=10.0, step=1.0)
    H = st.sidebar.number_input("Minimum Grade of Service - H", value=1.0, step=0.01)
    B = st.sidebar.number_input("Objective Grade of Service - B", value=0.001, step=0.0001, format="%0.5f")


    max_trunks = st.sidebar.number_input("Maximum Number of Trunks", value=35, step=1)

    results = erlang_b(A, H, B, max_trunks)

    st.write("### Results")
    df = pd.DataFrame(results, columns=["Trunks", "Offered", "Carried", "Cumulative", "P = G/S"])
    st.dataframe(df,hide_index=True, use_container_width=True, height=735)

    fig1, ax1 = plt.subplots(figsize=(8, 6))
    ax1.plot(df["Trunks"], df["Offered"], marker="o")
    ax1.set_xlabel("Trunks")
    ax1.set_ylabel("Offered Traffic (Erlang)")
    ax1.set_title("Offered vs Trunks")

    fig2, ax2 = plt.subplots(figsize=(8, 6))
    ax2.plot(df["Trunks"], df["Carried"], marker="o", color="orange")
    ax2.set_xlabel("Trunks")
    ax2.set_ylabel("Carried Traffic (Erlang)")
    ax2.set_title("Carried vs Trunks")

    fig3, ax3 = plt.subplots(figsize=(8, 6))
    ax3.plot(df["Trunks"], df["Cumulative"], marker="o", color="green")
    ax3.set_xlabel("Trunks")
    ax3.set_ylabel("Cumulative Traffic (Erlang)")
    ax3.set_title("Cumulative vs Trunks")

    fig4, ax4 = plt.subplots(figsize=(8, 6))
    ax4.plot(df["Trunks"], df["P = G/S"], marker="o", color="red")
    ax4.set_xlabel("Trunks")
    ax4.set_ylabel("P = G/S")
    ax4.set_title("P vs Trunks")

    # Display plots
    st.write("### Visualize in Graphs")
    st.pyplot(fig1)
    st.pyplot(fig2)
    st.pyplot(fig3)
    st.pyplot(fig4)

    st.title("Dynamic X and Y Axis Plot")
    with st.container():
        st.header("Select Data")

        x_axis = st.selectbox("Select X-axis data:", ["Trunks", "Offered", "Carried", "Cumulative", "P = G/S"])
        y_axis = st.selectbox("Select Y-axis data:", ["Trunks", "Offered", "Carried", "Cumulative", "P = G/S"])

        fig5, ax5 = plt.subplots(figsize=(8, 6))
        ax5.plot(df[f"{x_axis}"], df[f"{y_axis}"], marker="o", color="red")
        ax5.set_xlabel(f"{x_axis}")
        ax5.set_ylabel(f"{y_axis}")
        ax5.set_title(f"{y_axis} vs {x_axis}")
        st.pyplot(fig5)

if __name__ == "__main__":
    main()
