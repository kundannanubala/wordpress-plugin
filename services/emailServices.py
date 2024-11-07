from models.emailModel import EmailRequest  
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from google.cloud import aiplatform
from core.config import settings
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
# Email Prompt Template
def email_prompt_template():
    email_prompt="""You are tasked with generating a dynamic and personalized email for our company to its customers. Follow the steps below to ensure clarity, accuracy, and coherence. Avoid hallucination by strictly adhering to the provided variables from the context.

    Context:

    {context}

    Variables:

    Audience Context Keywords: {audience_context_keywords}
    Tone Keywords: {tone_keywords}
    Offer Elements: {offer_elements}
    Personalization Elements: {personalization_elements}
    Site Name: {site_name}
    Product to Endorse: {product_to_endorse}
    Customer Name: {customer_name}
    Purchase History: {purchase_history}
    Custom Discount Code: {custom_discount_code}
    Personalized Recommendations: {personalized_recommendations}
    PS Content: {ps_content}
    Source/Link: {source_link}
    Email Structural Elements and Instructions:

    Subject

    Variables Involved: Audience Context Keywords, Offer Elements, Site Name
    Instructions: Create a brief, eye-catching subject line that grabs attention. Wordplay is encouraged within reasonable bounds.
    Opening Greeting

    Variables: Customer Name, Purchase History, Audience Context Keywords, Tone Keywords
    Instructions: Write a formal opening for the email body. Base it on the customer's purchase history, mention the audience type, and clearly establish the agenda of the email while keeping it to the point.
    Benefits List

    Variables: Offer Elements, Product to Endorse, Purchase History
    Instructions: Present a list of benefits to tempt and persuade the customer. Spark interest based on their purchase history.
    Call-to-Action

    Variables: Source/Link, Purchase History, Tone Keywords
    Instructions: Persuade the customer to take action. Clearly mention why they should do so in an unambiguous and brief manner.
    Gratitude Statement

    Variables: Site Name, Tone Keywords
    Instructions: Express gratitude in an impactful way to leave a lasting impression and thought for the user.
    P.S. Section

    Variables: PS Content
    Instructions: Keep it brief.
    JSON Output Format

    Instructions for Output:

    Ensure each section follows the instructions and utilizes the appropriate variables.
    The "benefits_list" should be an array of strings, each representing a separate benefit.
    All text values should be strings.
    Maintain consistency in tone and style throughout the email.
    Do not include any additional commentary or explanation outside the JSON structure.
    Generate the email content based on the variables provided."""

    return email_prompt

async def email_generation(email_request: EmailRequest):
    try:
        # Initialize the Vertex AI client
        aiplatform.init(project=settings.GOOGLE_CLOUD_PROJECT)

        # Initialize the LLM
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-002", temperature=0.2, max_output_tokens=4096, top_p=0.95, top_k=40)

        # Use the email_prompt_template function to generate the email content
        email_prompt = email_prompt_template().format(
            context=email_request.context or "No context provided",
            audience_context_keywords=", ".join(email_request.audience_context_keywords) if email_request.audience_context_keywords else "No keywords",
            tone_keywords=", ".join(email_request.tone_keywords) if email_request.tone_keywords else "No tone keywords",
            offer_elements=", ".join(email_request.offer_elements) if email_request.offer_elements else "No offer elements",
            personalization_elements=", ".join(email_request.personalization_elements) if email_request.personalization_elements else "No personalization elements",
            site_name=email_request.site_name or "No site name",
            product_to_endorse=email_request.product_to_endorse or "No product",
            customer_name=email_request.customer_name or "No customer name",
            purchase_history=email_request.purchase_history or "No purchase history",
            custom_discount_code=email_request.custom_discount_code or "No discount code",
            personalized_recommendations=", ".join(email_request.personalized_recommendations) if email_request.personalized_recommendations else "No recommendations",
            ps_content=email_request.ps_content or "No PS content",
            source_link=email_request.source_link or "No source link"
        )
        prompt = ChatPromptTemplate.from_template(email_prompt)
        context = {"context": lambda x: email_prompt}
        chain = (
            context
            | prompt
            | llm
            | StrOutputParser()
        )
        result = await asyncio.to_thread(chain.invoke, context)
        return result
    except Exception as e:
        raise e
        
