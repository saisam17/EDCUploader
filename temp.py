import excel2flapjack.main as e2f
import excel2sbol.converter as conv
import tempfile
import requests
import os
      
fj_url = "flapjack.rudge-lab.org:8000"
fj_user = "sai"
fj_pass = "123"

direct = os.path.split(__file__)[0]
file_path = os.path.join(direct, 'flapjack_excel_converter_v028.xlsx')
file_path_out = os.path.join(direct, 'test.xml')


# upload the excel file to flapjack and get hash map back
hash_map = e2f.flapjack_upload(fj_url, fj_user, fj_pass, file_path)
print(hash_map)

# convert the excel file to SBOL
# use excel2sbol - could ask for an update that just gives the doc back rather than the file
conv.converter(file_path, file_path_out)


# Add flapjack annotations to the SBOL
# use pysbol2 documentation: https://pysbol.readthedocs.io/en/stable/introduction.html

# Upload the file to SBH
# documentation: https://wiki.synbiohub.org/api-docs/#submit and https://wiki.synbiohub.org/api-docs/#login


# Pull uris from synbiohub

# Add uris to flapjack