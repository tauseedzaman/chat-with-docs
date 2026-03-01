from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import Chroma
from app.rag.embeddings import get_embeddings
from app.rag.llm import get_llm
from app.config import settings

def get_rag_chain():
    vectorstore = Chroma(
        persist_directory=settings.CHROMA_DB_DIR,
        embedding_function=get_embeddings()
    )
    
    retriever = vectorstore.as_retriever()
    llm = get_llm()
    
    system_prompt = (
        "You are an assistant for question-answering tasks. Your name is DudeX2. "
        "Use the following pieces of retrieved context to answer the question. "
        "If the information is not present in the context below, "
        "respond exactly with: 'I could not find this information in the uploaded documents.' "
        "Do not use any other information. "
        "Use three sentences maximum and keep the answer concise."
        "\n\n"
        "{context}"
    )
    
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )
    
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    rag_chain = (
        {
            "context": retriever | format_docs, 
            "input": RunnablePassthrough(),
            "raw_context": retriever  # Extra field to get the original objects
        }
        | RunnablePassthrough.assign(
            answer = prompt | llm | StrOutputParser()
        )
    )
    
    return rag_chain
