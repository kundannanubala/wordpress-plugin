from pydantic import BaseModel
from typing import List

class EmailRequest(BaseModel):
    context: str
    audience_context_keywords: List[str]
    tone_keywords: List[str]
    offer_elements: List[str]
    personalization_elements: List[str]
    site_name: str
    product_to_endorse: str
    customer_name: str
    purchase_history: str
    custom_discount_code: str
    personalized_recommendations: List[str]
    ps_content: str
    source_link: str