from transformers.agents import Tool

class RetrieverTool(Tool):
    name = "retriever"
    description = "This function utilizes semantic similarity to retrieve documents from the knowledge base that have the closest match to the input query"
    inputs = {
        "query": {
            "type": "text",
            "description": "The query should be semantically aligned with the desired documents and phrased in the affirmative.",
        }
    }
    output_type = "text"

    def __init__(self, vectordb, **kwargs):
        super().__init__(**kwargs)
        self.vectordb = vectordb

    def forward(self, query: str) -> str:
        assert isinstance(query, str), "Your search query must be a string"

        docs = self.vectordb.similarity_search(
            query,
            k=7,
        )

        return "\nRetrieved documents:\n" + "".join(
            [f"===== Document {str(i)} =====\n" + doc.page_content for i, doc in enumerate(docs)]
        )