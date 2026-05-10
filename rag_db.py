import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="ai_docs")

# -------------------------
# PART 3: SEED DATA
# -------------------------
docs = [
    "AI in healthcare improves diagnosis accuracy.",
    "Machine learning helps predict diseases early.",
    "Deep learning is used in medical imaging.",
    "AI chatbots assist patient communication.",
    "Data privacy is important in healthcare AI.",
    "AI reduces workload for doctors.",
    "Natural language processing helps analyze reports.",
    "AI improves drug discovery process.",
    "Computer vision helps detect tumors.",
    "AI supports personalized treatment plans."
]

for i, doc in enumerate(docs):
    collection.add(
        documents=[doc],
        ids=[f"doc_{i}"]
    )

print("ChromaDB seeded successfully")

# -------------------------
# PART 4: TEST QUERY (ADD HERE)
# -------------------------

query = "How AI helps in healthcare?"

results = collection.query(
    query_texts=[query],
    n_results=3
)

print("Search Results:")
print(results)