# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import pandas as pd
from polygon import WebSocketClient 
from polygon.websocket.models import WebSocketMessage 
from typing import List 
from polygon.websocket.models.common import Feed, Market
import asyncio
import json

import nest_asyncio
from requests import Response
import responses

# Create your views here.
nest_asyncio.apply()

pd.set_option('display.max_rows', None)

# global previous_type, df_T, df_Q
# global bidsize, bidprice, askprice, asksize
# global sum_price, sum_size, count_T
sum_price = 1
sum_size = 1
count_T = 1
bidsize = 1
bidprice = 1
askprice = 1
asksize = 1

trades0 = {}
quotes0 = {}
ask_quotes0 = {}

trades1 = {}
quotes1 = {}
ask_quotes1 = {}

trades2 = {}
quotes2 = {}
ask_quotes2 = {}


trades3 = {}
quotes3 = {}
ask_quotes3 = {}

trades4 = {}
quotes4 = {}
ask_quotes4 = {}

trades5 = {}
quotes5 = {}
ask_quotes5 = {}

trades6 = {}
quotes6 = {}
ask_quotes6 = {}

previous_type0 = 'T' 

# TSLA
df_T0 = pd.DataFrame([], columns = ['event_type', 'symbol', 'exchange', 'id', 'tape', 'price', 'size',
                   'conditions', 'timestamp', 'sequence_number'])
df_Q0 = pd.DataFrame([], columns = ['event_type', 'symbol', 'bid_exchange_id', 'bid_price',
                               'bid_size', 'ask_exchange_id', 'ask_price', 'ask_size', 'condition', 'timestamp',
                               'tape', 'sequence_number'])
# AAPL
df_T1 = pd.DataFrame([], columns = ['event_type', 'symbol', 'exchange', 'id', 'tape', 'price', 'size',
                   'conditions', 'timestamp', 'sequence_number'])
df_Q1 = pd.DataFrame([], columns = ['event_type', 'symbol', 'bid_exchange_id', 'bid_price',
                               'bid_size', 'ask_exchange_id', 'ask_price', 'ask_size', 'condition', 'timestamp',
                               'tape', 'sequence_number'])
# AMZN
df_T2 = pd.DataFrame([], columns = ['event_type', 'symbol', 'exchange', 'id', 'tape', 'price', 'size',
                   'conditions', 'timestamp', 'sequence_number'])
df_Q2 = pd.DataFrame([], columns = ['event_type', 'symbol', 'bid_exchange_id', 'bid_price',
                               'bid_size', 'ask_exchange_id', 'ask_price', 'ask_size', 'condition', 'timestamp',
                               'tape', 'sequence_number'])

# AMD
df_T3 = pd.DataFrame([], columns = ['event_type', 'symbol', 'exchange', 'id', 'tape', 'price', 'size',
                   'conditions', 'timestamp', 'sequence_number'])
df_Q3 = pd.DataFrame([], columns = ['event_type', 'symbol', 'bid_exchange_id', 'bid_price',
                               'bid_size', 'ask_exchange_id', 'ask_price', 'ask_size', 'condition', 'timestamp',
                               'tape', 'sequence_number'])

# GOOGL
df_T4 = pd.DataFrame([], columns = ['event_type', 'symbol', 'exchange', 'id', 'tape', 'price', 'size',
                   'conditions', 'timestamp', 'sequence_number'])
df_Q4 = pd.DataFrame([], columns = ['event_type', 'symbol', 'bid_exchange_id', 'bid_price',
                               'bid_size', 'ask_exchange_id', 'ask_price', 'ask_size', 'condition', 'timestamp',
                               'tape', 'sequence_number'])

# META
df_T5 = pd.DataFrame([], columns = ['event_type', 'symbol', 'exchange', 'id', 'tape', 'price', 'size',
                   'conditions', 'timestamp', 'sequence_number'])
df_Q5 = pd.DataFrame([], columns = ['event_type', 'symbol', 'bid_exchange_id', 'bid_price',
                               'bid_size', 'ask_exchange_id', 'ask_price', 'ask_size', 'condition', 'timestamp',
                               'tape', 'sequence_number'])

# GOOG
df_T6 = pd.DataFrame([], columns = ['event_type', 'symbol', 'exchange', 'id', 'tape', 'price', 'size',
                   'conditions', 'timestamp', 'sequence_number'])
df_Q6 = pd.DataFrame([], columns = ['event_type', 'symbol', 'bid_exchange_id', 'bid_price',
                               'bid_size', 'ask_exchange_id', 'ask_price', 'ask_size', 'condition', 'timestamp',
                               'tape', 'sequence_number'])

def handle_msg(msgs: List[WebSocketMessage]): 
    global previous_type0, df_T0,df_T1,df_T2, df_T3,df_T4,df_T5,df_T6, df_Q0, df_Q1,df_Q2, df_Q3, df_Q4,df_Q5,df_Q6
    global ask_quotes0, ask_quotes1, ask_quotes2, ask_quotes3, ask_quotes4, ask_quotes5, ask_quotes6
    global trades0, trades1, trades2, trades3, trades4, trades5, trades6
    global quotes0, quotes1, quotes2, quotes3, quotes4, quotes5, quotes6

    for m in msgs:
        #print("\n\n")
        temp_df = pd.DataFrame([m],)
        #print(temp_df)
        temp_e_t = temp_df['event_type'][0] 
        temp_symbol = temp_df['symbol'][0]
        print(temp_symbol)
        #print(temp_e_t)
        #print(previous_type)
        if temp_e_t == 'T':
            if temp_symbol == "TSLA":
                df_T0 = pd.concat([df_T0 ,temp_df], ignore_index=True)
            elif temp_symbol == "AAPL":
                df_T1 = pd.concat([df_T1 ,temp_df], ignore_index=True)
            elif temp_symbol == "AMZN":
                df_T2 = pd.concat([df_T2 ,temp_df], ignore_index=True)
            if temp_symbol == "AMD":
                df_T3 = pd.concat([df_T3 ,temp_df], ignore_index=True)
            elif temp_symbol == "GOOGL":
                df_T4 = pd.concat([df_T4 ,temp_df], ignore_index=True)
            elif temp_symbol == "META":
                df_T5 = pd.concat([df_T5 ,temp_df], ignore_index=True)
            elif temp_symbol == "GOOG":
                df_T6 = pd.concat([df_T6 ,temp_df], ignore_index=True)

            #print(len(df_T))
        elif temp_e_t == 'Q':
            if temp_symbol == "TSLA":
                df_Q0 = pd.concat([df_Q0 ,temp_df], ignore_index=True)
            elif temp_symbol == "AAPL":
                df_Q1 = pd.concat([df_Q1 ,temp_df], ignore_index=True)
            elif temp_symbol == "AMZN":
                df_Q2 = pd.concat([df_Q2 ,temp_df], ignore_index=True)
            if temp_symbol == "AMD":
                df_Q3 = pd.concat([df_Q3 ,temp_df], ignore_index=True)
            elif temp_symbol == "GOOGL":
                df_Q4 = pd.concat([df_Q4 ,temp_df], ignore_index=True)
            elif temp_symbol == "META":
                df_Q5 = pd.concat([df_Q5 ,temp_df], ignore_index=True)
            elif temp_symbol == "GOOG":
                df_Q6 = pd.concat([df_Q6 ,temp_df], ignore_index=True)

        ## check event type as previous event type
        if previous_type0 != temp_e_t:
            ## in case of TTT..TT -> A: it should print sum of T
            if temp_e_t == 'Q':
                ## calculate sum of price and size for A
                global sum_price, sum_size, count_T
                sum_price = df_T0['price'].sum()
                sum_size = df_T0['size'].sum()
                count_T = len(df_T0)
                ## add printing condition
                if sum_size >= 1:
                    print("\n\n*** T : ", " Sum of Price = ", sum_price,", Sum of Size = " , sum_size, ", Count :" ,count_T)

                    if temp_symbol == "TSLA":
                        result = df_T0[['price', 'size']].groupby(['price']).agg(['sum', 'count'])
                        trades0 = json.dumps(json.loads(result.to_json(orient="index")), indent=4)
                    elif temp_symbol == "AAPL":
                        result = df_T1[['price', 'size']].groupby(['price']).agg(['sum', 'count'])
                        trades1 = json.dumps(json.loads(result.to_json(orient="index")), indent=4)
                    elif temp_symbol == "AMZN":
                        result = df_T2[['price', 'size']].groupby(['price']).agg(['sum', 'count'])
                        trades2 = json.dumps(json.loads(result.to_json(orient="index")), indent=4)
                    if temp_symbol == "AMD":
                        result = df_T3[['price', 'size']].groupby(['price']).agg(['sum', 'count'])
                        trades3 = json.dumps(json.loads(result.to_json(orient="index")), indent=4)
                    elif temp_symbol == "GOOGL":
                        result = df_T4[['price', 'size']].groupby(['price']).agg(['sum', 'count'])
                        trades4 = json.dumps(json.loads(result.to_json(orient="index")), indent=4)
                    elif temp_symbol == "META":
                        result = df_T5[['price', 'size']].groupby(['price']).agg(['sum', 'count'])
                        trades5 = json.dumps(json.loads(result.to_json(orient="index")), indent=4)
                    elif temp_symbol == "GOOG":
                        result = df_T6[['price', 'size']].groupby(['price']).agg(['sum', 'count'])
                        trades6 = json.dumps(json.loads(result.to_json(orient="index")), indent=4)

                # df_T0 = pd.DataFrame([], columns = ['event_type', 'symbol', 'exchange', 'id', 'tape', 'price', 'size',
                #        'conditions', 'timestamp', 'sequence_number'])
                # df_T1 = pd.DataFrame([], columns = ['event_type', 'symbol', 'exchange', 'id', 'tape', 'price', 'size',
                #        'conditions', 'timestamp', 'sequence_number'])
                # df_T2 = pd.DataFrame([], columns = ['event_type', 'symbol', 'exchange', 'id', 'tape', 'price', 'size',
                #        'conditions', 'timestamp', 'sequence_number'])
                previous_type0 = 'Q'
            ## in case of AAA -> T, then it should print sum of A
            elif temp_e_t == 'T':
                global bidsize, bidprice, askprice, asksize
                bidsize = df_Q0['bid_size'].sum()
                bidprice = df_Q0['bid_price'].sum()
                askprice = df_Q0['ask_price'].sum()
                asksize = df_Q0['ask_size'].sum()
                count_Q = len(df_Q0)
                if bidsize >= 1:
                    print("\n###  Q : Sum of bidprice=", bidprice,",Sum of bidsize=",bidsize,',Count=', count_Q)
                    if temp_symbol == "TSLA":
                        result = df_Q0[['bid_price', 'bid_size']].groupby(['bid_price']).agg(['sum', 'count'])
                        quotes0 = json.dumps(json.loads(result.to_json(orient="index")), indent=4)
                    elif temp_symbol == "AAPL":
                        result = df_Q1[['bid_price', 'bid_size']].groupby(['bid_price']).agg(['sum', 'count'])
                        quotes1 = json.dumps(json.loads(result.to_json(orient="index")), indent=4)
                    elif temp_symbol == "AMZN":
                        result = df_Q2[['bid_price', 'bid_size']].groupby(['bid_price']).agg(['sum', 'count'])
                        quotes2 = json.dumps(json.loads(result.to_json(orient="index")), indent=4)
                    if temp_symbol == "AMD":
                        result = df_Q3[['bid_price', 'bid_size']].groupby(['bid_price']).agg(['sum', 'count'])
                        quotes3 = json.dumps(json.loads(result.to_json(orient="index")), indent=4)
                    elif temp_symbol == "GOOGL":
                        result = df_Q4[['bid_price', 'bid_size']].groupby(['bid_price']).agg(['sum', 'count'])
                        quotes4 = json.dumps(json.loads(result.to_json(orient="index")), indent=4)
                    elif temp_symbol == "META":
                        result = df_Q5[['bid_price', 'bid_size']].groupby(['bid_price']).agg(['sum', 'count'])
                        quotes5 = json.dumps(json.loads(result.to_json(orient="index")), indent=4)
                    elif temp_symbol == "GOOG":
                        result = df_Q6[['bid_price', 'bid_size']].groupby(['bid_price']).agg(['sum', 'count'])
                        quotes6 = json.dumps(json.loads(result.to_json(orient="index")), indent=4)

                if asksize >= 1:
                    print('\n###  Q :,Sum of askprice=',askprice,',Sum of asksize=',asksize ,',Count=', count_Q)

                    if temp_symbol == "TSLA":
                        result = df_Q0[['ask_price', 'ask_size']].groupby(['ask_price']).agg(['sum', 'count'])
                        ask_quotes0 = json.dumps(json.loads(result.to_json(orient="index")), indent=4)
                    elif temp_symbol == "AAPL":
                        result = df_Q1[['ask_price', 'ask_size']].groupby(['ask_price']).agg(['sum', 'count'])
                        ask_quotes1 = json.dumps(json.loads(result.to_json(orient="index")), indent=4)
                    elif temp_symbol == "AMZN":
                        result = df_Q2[['ask_price', 'ask_size']].groupby(['ask_price']).agg(['sum', 'count'])
                        ask_quotes2 = json.dumps(json.loads(result.to_json(orient="index")), indent=4)
                    if temp_symbol == "AMD":
                        result = df_Q3[['ask_price', 'ask_size']].groupby(['ask_price']).agg(['sum', 'count'])
                        ask_quotes3 = json.dumps(json.loads(result.to_json(orient="index")), indent=4)
                    elif temp_symbol == "GOOGL":
                        result = df_Q4[['ask_price', 'ask_size']].groupby(['ask_price']).agg(['sum', 'count'])
                        ask_quotes4 = json.dumps(json.loads(result.to_json(orient="index")), indent=4)
                    elif temp_symbol == "META":
                        result = df_Q5[['ask_price', 'ask_size']].groupby(['ask_price']).agg(['sum', 'count'])
                        ask_quotes5 = json.dumps(json.loads(result.to_json(orient="index")), indent=4)
                    elif temp_symbol == "GOOG":
                        result = df_Q6[['ask_price', 'ask_size']].groupby(['ask_price']).agg(['sum', 'count'])
                        ask_quotes6 = json.dumps(json.loads(result.to_json(orient="index")), indent=4)

                # df_Q0 = pd.DataFrame([], columns = ['event_type', 'symbol', 'bid_exchange_id', 'bid_price',
                #                'bid_size', 'ask_exchange_id', 'ask_price', 'ask_size', 'condition', 'timestamp',
                #                'tape', 'sequence_number'])
                # df_Q1 = pd.DataFrame([], columns = ['event_type', 'symbol', 'bid_exchange_id', 'bid_price',
                #                'bid_size', 'ask_exchange_id', 'ask_price', 'ask_size', 'condition', 'timestamp',
                #                'tape', 'sequence_number'])
                # df_Q2 = pd.DataFrame([], columns = ['event_type', 'symbol', 'bid_exchange_id', 'bid_price',
                #                'bid_size', 'ask_exchange_id', 'ask_price', 'ask_size', 'condition', 'timestamp',
                #                'tape', 'sequence_number'])

                previous_type0 = 'T'               
    # asyncio.run(c.close())
    # global test
    # test = df_Q[['ask_price', 'ask_size']].groupby(['ask_price']).agg(['sum', 'count']).to_html()

def get_data(request):
    global c
    c = WebSocketClient(api_key='3zSpRl4TaFgSyg0nm7gsC9Blgs52MWmu', feed='socket.polygon.io',
                    market='stocks',  subscriptions=["Q.TSLA","T.TSLA", "Q.AAPL","T.AAPL" , "Q.AMZN","T.AMZN","Q.META","T.META","Q.GOOGL","T.GOOGL","Q.AMD","T.AMD","Q.GOOG","T.GOOG"]) 

    c.run(handle_msg)
    return HttpResponse("test")


def get_contents(request):
    data = {
        'trades0': trades0,
        'quotes0': quotes0,
        'ask_quotes0': ask_quotes0,
        'trades1': trades1,
        'quotes1': quotes1,
        'ask_quotes1': ask_quotes1,
        'trades2': trades2,
        'quotes2': quotes2,
        'ask_quotes2': ask_quotes2,
        'trades3': trades3,
        'quotes3': quotes3,
        'ask_quotes3': ask_quotes3,
        'trades4': trades4,
        'quotes4': quotes4,
        'ask_quotes4': ask_quotes4,
        'trades5': trades5,
        'quotes5': quotes5,
        'ask_quotes5': ask_quotes5,
        'trades6': trades6,
        'quotes6': quotes6,
        'ask_quotes6': ask_quotes6,

    }
    return HttpResponse(json.dumps(data))


def dashboard(request):
    template = loader.get_template('dashboard.html')

    return HttpResponse(template.render())
