"""

The REST API permits the retrieval of all data for one core object at a time.

GraphQL API (GraphiQL interface)
The GraphQL interface offers more flexible data retrieval,
essentially making it possible to grab any piece of data from any level of the hierarchy
in a single query. To use it programmatically POST your GraphQL queries under the
data.rcsb.org/graphql endpoint. All output from both REST and GraphQL interfaces is offered
in JSON format.

Search API
The search API programmatically exposes all search functionality available at rcsb.org.
It is possible to perform queries with arbitrary Boolean logic across all data available
in the RCSB PDB data API via a convenient JSON-format query language. At the root level it
is also possible to combine text-based searches (any text/numerical field in the RCSB PDB
data API) with protein/nucleotide sequence search (mmseqs2 software) and Structure similarity
searches (BioZernike software, described in Guzenko et al 2020). All output from the Search
API is offered in JSON format.

Database schema is here:
http://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Index/

    entry:

"""

import requests


def run_graphql_query(query):
    # https://gist.github.com/gbaman/b3137e18c739e0cf98539bf4ec4366ad
    # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('http://data.rcsb.org/graphql', json={'query': query})
    print(request.url)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(f"Query failed to run by returning code of {request.status_code}. {query}")


def uniprot_id(pdbid, entityid):
    query = f"""
    {{
      polymer_entity(entry_id: "{pdbid}", entity_id: "{entityid}") {{
        uniprots {{
          rcsb_id
        }}
      }}
    }} 
    """

    result = run_graphql_query(query)
    return result["data"]["polymer_entity"]["uniprots"][0]["rcsb_id"]


def uniprot_alignment(pdbid, entityid):
    query = f"""
    {{
      polymer_entity(entry_id: "{pdbid}", entity_id: "{entityid}") {{
        rcsb_polymer_entity_align {{
          aligned_regions {{
            entity_beg_seq_id
            length
            ref_beg_seq_id
          }}
        }}
      }}
    }}
    """
    result = run_graphql_query(query)
    return dict(result["data"]["polymer_entity"]["rcsb_polymer_entity_align"][0]["aligned_regions"][0])



if __name__ == "__main__":
    print(uniprot_id("6y2g", "1"))
    # print(uniprot_alignment("1aq1", "1"))
    #
    # request = requests.get("https://www.uniprot.org/uniprot/P0DTD1.fasta")
    # request.text
    # #