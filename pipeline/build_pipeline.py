from dotenv import load_dotenv
from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting to build pipeline...")

        loader = AnimeDataLoader("data/anime_with_synopsis.csv", "data/anime_updated.csv")
        processed_csv = loader.load_process()

        logger.info("Data loaded and processed successfully.")

        vector_builder = VectorStoreBuilder(processed_csv)
        vector_builder.build_save_vectorstore()

        logger.info("Vector store built successfully.")
        logger.info("Pipeline built successfully.")
        
    except Exception as e:
        logger.error(f"Failed to execute pipeline: {str(e)}")
        raise CustomException("Error during pipeline execution", e)
    
if __name__ == "__main__":
    main()
