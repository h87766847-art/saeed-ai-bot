# knowledge_graph_engine.py
# Saeed Core
# Advanced Knowledge Graph System


import datetime
import uuid





NODES = {}

EDGES = {}







def create_node(

        name,

        category="general",

        data=None

):


    node_id = str(

        uuid.uuid4()

    )



    NODES[node_id] = {


        "id":

        node_id,


        "name":

        name,


        "category":

        category,


        "data":

        data,


        "created":

        str(

            datetime.datetime.now()

        )

    }



    return NODES[node_id]









def connect_nodes(

        node_a,

        node_b,

        relation

):


    edge_id = str(

        uuid.uuid4()

    )



    EDGES[edge_id] = {


        "from":

        node_a,


        "to":

        node_b,


        "relation":

        relation,


        "created":

        str(

            datetime.datetime.now()

        )

    }



    return EDGES[edge_id]









def get_node(

        node_id

):


    return NODES.get(

        node_id,

        None

    )








def find_by_name(

        name

):


    results = []



    for node in NODES.values():


        if node["name"] == name:


            results.append(

                node

            )



    return results







def get_connections(

        node_id

):


    connections = []



    for edge in EDGES.values():


        if (

            edge["from"] == node_id

            or

            edge["to"] == node_id

        ):


            connections.append(

                edge

            )



    return connections







def graph_status():


    return {


        "nodes":

        len(NODES),


        "connections":

        len(EDGES),


        "status":

        "active"

    }
