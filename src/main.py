import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def simulate_population(gen0, generations, mutation_rate=0.01):
    history = [gen0]
    current = gen0.copy()

    for _ in range(generations):
        parents = current[np.random.randint(0, len(current), (len(current), 2))]
        offspring = []

        for p1, p2 in parents:
            child = [
                np.random.choice(p1),
                np.random.choice(p2)
            ]
            # Mutation chance
            if np.random.rand() < mutation_rate:
                child[np.random.randint(0, 2)] = np.random.choice(["A", "a"])
            offspring.append(child)

        current = np.array(offspring)
        history.append(current)

    return history

def calculate_frequencies(population_history):
    freqs = []

    for pop in population_history:
        alleles = pop.flatten()
        A_count = np.sum(alleles == "A")
        a_count = np.sum(alleles == "a")
        total = len(alleles)
        freqs.append((A_count / total, a_count / total))

    return np.array(freqs)

def main():
    st.title("🧬 Genetics Simulator (NumPy)")

    pop_size = st.slider("Initial Population Size", 10, 1000, 100)
    generations = st.slider("Number of Generations", 1, 100, 50)
    mutation_rate = st.slider("Mutation Rate", 0.0, 0.1, 0.01)

    if st.button("Run Simulation"):
        gen0 = np.random.choice(["A", "a"], size=(pop_size, 2), p=[0.5, 0.5])
        history = simulate_population(gen0, generations, mutation_rate)
        freqs = calculate_frequencies(history)

        st.write("📈 Allele Frequency Over Generations")
        fig, ax = plt.subplots()
        ax.plot(freqs[:, 0], label="A", color="blue")
        ax.plot(freqs[:, 1], label="a", color="red")
        ax.set_xlabel("Generation")
        ax.set_ylabel("Frequency")
        ax.legend()
        st.pyplot(fig)

if __name__ == "__main__":
    main()