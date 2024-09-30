from core.config import app
from database.data_helpers import get_product_embeddings
import uvicorn

from api.endpoints import handle_new_chat_message_from_user, get_products_by_description
if __name__ == "__main__":
  #get_product_embeddings()
  uvicorn.run(app, host="0.0.0.0", port=8000)