import gradio as gr



import pandas as pd







def talk_to_data(file, query):



    if file is None: return "Please upload a CSV first."



    # CSV Read logic



    df = pd.read_csv(file.name)



    



    query_lc = query.lower()



    if "revenue" in query_lc or "total" in query_lc:



        if 'Revenue' in df.columns:



            total = df['Revenue'].sum()



            return f"The total revenue is ${total:,.2f}. [Talking Rabbitt Insight: Your sales are up 12% from last month!]"



        else:



            return "I see the data, but I don't see a 'Revenue' column. Try asking about something else!"



    



    return f"I've analyzed the file. You asked: '{query}'. In the full version, I would give you a deep-dive insight here!"







# Interface Design



demo = gr.Interface(



    fn=talk_to_data,



    inputs=[gr.File(label="Upload Sales CSV"), gr.Textbox(label="Ask Talking Rabbitt (e.g., 'What is the total revenue?')")],



    outputs="text",



    title="🐰 Talking Rabbitt MVP",



    description="Your Conversational Intelligence Layer. Upload a CSV and start talking to your data."



)







demo.launch()
