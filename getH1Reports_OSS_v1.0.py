import requests
import csv
import time
import pyodbc
import cursor
import sys

############################################################################################
def getReports(auth_name, auth_key, program_name, page_size, page_number):
  try:
    headers = {'Accept': 'application/json'}
    condition_filter = "filter[program][]={}&page[size]={}&page[number]={}".format(program_name, page_size, page_number)
    url = 'https://api.hackerone.com/v1/reports?' + condition_filter  
    response = requests.get(url, auth=(auth_name, auth_key), headers = headers)
    return(response.json())
  except Exception as e:
    print("Error in getReports(): " + str(e))
    exit()

############################################################################################
def spinRod(rod):

  if (rod == ""):
    rod = "/"
  elif (rod == "/"):
    rod = "-"
  elif (rod == "-"):
    rod = "\\"
  elif (rod == "\\"):
    rod = "|"
  elif (rod == "|"):
    rod = "/"
  else:
    rod = "/"  
  
  print("processing records " + rod, end='\r')  
  time.sleep(.05) 
  return(rod)        

############################################################################################
def processReports(program_name, jsonResponse, conCursor):
  
  rod = ""

  for key in range(len(jsonResponse['data'])):
    
    rod = spinRod(rod)

    try:
      # reset variables
      reportCustomFieldSubTakeover = ''
      reportCustomFieldIPaddress = ''
      ipAddressCountry = ''
      ipAddressCountryCode = ''
      ipAddressCity = ''
      ipAddressRegion = ''
      ipAddressPostalCode = ''
      ipAddressLatitude = ''
      ipAddressLongitude = ''

      for customField in jsonResponse['data'][key]['relationships']['custom_field_values']['data']:
        if(customField['relationships']['custom_field_attribute']['data']['attributes']['label'] == "Your IP Address"):
          reportCustomFieldIPaddress = customField['attributes']['value'].strip()

    except Exception as e:
      ipAddressCountry = ''
      ipAddressCountryCode = ''
      ipAddressCity = ''
      ipAddressRegion = ''
      ipAddressPostalCode = ''
      ipAddressLatitude = ''
      ipAddressLongitude = ''

    try:
      reportId                            = jsonResponse['data'][key]['id']                                                           
    except Exception as e: 
      reportId = ""

    try:
      reportState                         = jsonResponse['data'][key]['attributes']['state']                                          
    except Exception as e: 
      reportState = ""

    try:
      reportCreatedDateTime               = jsonResponse['data'][key]['attributes']['created_at']                                     
    except Exception as e: 
      reportCreatedDateTime = ""

    try:
      reportVulnerabilityInformation   = jsonResponse['data'][key]['attributes']['vulnerability_information'] 
    except Exception as e:
      reportVulnerabilityInformation = ""
    
    try:
      reportTitle                         = jsonResponse['data'][key]['attributes']['title']                                          
    except Exception as e: 
      reportTitle = ""
    
    try:
      reportTriagedDateTime               = jsonResponse['data'][key]['attributes']['triaged_at']                                     
    except Exception as e: 
      reportTriagedDateTime = ""
    
    try:
      reportClosedDateTime                = jsonResponse['data'][key]['attributes']['closed_at']                                      
    except Exception as e: 
      reportClosedDateTime = ""
    
    try:
      reportLastReporterActivityDateTime  = jsonResponse['data'][key]['attributes']['last_reporter_activity_at']                      
    except Exception as e: 
      reportLastReporterActivityDateTime = ""
    
    try:
      reportFirstProgramActivityDateTime  = jsonResponse['data'][key]['attributes']['first_program_activity_at']                      
    except Exception as e: 
      reportFirstProgramActivityDateTime = ""
    
    try:
      reportLastProgramActivityDateTime   = jsonResponse['data'][key]['attributes']['last_program_activity_at']                       
    except Exception as e: 
      reportLastProgramActivityDateTime = ""
    
    try:
      reportBountyAwardedDateTime         = jsonResponse['data'][key]['attributes']['bounty_awarded_at']                              
    except Exception as e: 
      reportBountyAwardedDateTime = ""
    
    try:
      reportSwagAwardedDateTime           = jsonResponse['data'][key]['attributes']['swag_awarded_at']                                
    except Exception as e: 
      reportSwagAwardedDateTime = ""
    
    try:
      reportDisclosedDateTime             = jsonResponse['data'][key]['attributes']['disclosed_at']                                   
    except Exception as e: 
      reportDisclosedDateTime = ""
    
    try:
      reportLastPublicActivityDateTime    = jsonResponse['data'][key]['attributes']['last_public_activity_at']                        
    except Exception as e: 
      reportLastPublicActivityDateTime = ""
    
    try:
      reportLastActivityDateTime          = jsonResponse['data'][key]['attributes']['last_activity_at']                               
    except Exception as e: 
      reportLastActivityDateTime = ""
    
    try:
      reportIssueTrackerUrl               = jsonResponse['data'][key]['attributes']['issue_tracker_reference_url']                    
    except Exception as e: 
      reportIssueTrackerUrl = ""
    
    try:
      researcherUsername                  = jsonResponse['data'][key]['relationships']['reporter']['data']['attributes']['username']  
    except Exception as e: 
      researcherUsername = ""
    
    try:
      researcherName                      = jsonResponse['data'][key]['relationships']['reporter']['data']['attributes']['name']      
    except Exception as e: 
      researcherName = ""
    
    try:
      researcherReputation                = jsonResponse['data'][key]['relationships']['reporter']['data']['attributes']['reputation']              
    except Exception as e: 
      researcherReputation = ""
    
    try:
      researcherSignal                    = jsonResponse['data'][key]['relationships']['reporter']['data']['attributes']['signal']                  
    except Exception as e: 
      researcherSignal = ""
    
    try:
      researcherImpact                    = jsonResponse['data'][key]['relationships']['reporter']['data']['attributes']['impact']                  
    except Exception as e: 
      researcherImpact = ""
    
    try:      
      reportSeverityCVSSRating            = jsonResponse['data'][key]['relationships']['severity']['data']['attributes']['rating']                             
    except Exception as e: 
      reportSeverityCVSSRating = ""
    
    try:
      reportSeverityCVSSScore             = jsonResponse['data'][key]['relationships']['severity']['data']['attributes']['score']                              
    except Exception as e: 
      reportSeverityCVSSScore = ""
    
    try:
      reportSeverityCVSSSComplexity       = jsonResponse['data'][key]['relationships']['severity']['data']['attributes']['attack_complexity']                  
    except Exception as e: 
      reportSeverityCVSSSComplexity = ""
    
    try:
      reportSeverityCVSSSVector           = jsonResponse['data'][key]['relationships']['severity']['data']['attributes']['attack_vector']                      
    except Exception as e: 
      reportSeverityCVSSSVector = ""
    
    try:
      reportSeverityCVSSSAvailability     = jsonResponse['data'][key]['relationships']['severity']['data']['attributes']['availability']                       
    except Exception as e: 
      reportSeverityCVSSSAvailability = ""
    
    try:
      reportSeverityCVSSConfidentiality   = jsonResponse['data'][key]['relationships']['severity']['data']['attributes']['confidentiality']                    
    except Exception as e: 
      reportSeverityCVSSConfidentiality = ""
    
    try:
      reportSeverityCVSSIntegrity         = jsonResponse['data'][key]['relationships']['severity']['data']['attributes']['integrity']                          
    except Exception as e: 
      reportSeverityCVSSIntegrity = ""
    
    try:
      reportSeverityCVSSPrivileges        = jsonResponse['data'][key]['relationships']['severity']['data']['attributes']['privileges_required']                
    except Exception as e: 
      reportSeverityCVSSPrivileges = ""
    
    try:
      reportSeverityCVSSUserInteraction   = jsonResponse['data'][key]['relationships']['severity']['data']['attributes']['user_interaction']                   
    except Exception as e: 
      reportSeverityCVSSUserInteraction = ""
    
    try:
      reportSeverityCVSSScopeChange       = jsonResponse['data'][key]['relationships']['severity']['data']['attributes']['scope']                              
    except Exception as e: 
      reportSeverityCVSSScopeChange = ""
    
    try:
      reportWeaknessName                  = jsonResponse['data'][key]['relationships']['weakness']['data']['attributes']['name']                               
    except Exception as e: 
      reportWeaknessName = ""
    
    try:
      reportWeaknessCWEID                 = jsonResponse['data'][key]['relationships']['weakness']['data']['attributes']['external_id']                        
    except Exception as e: 
      reportWeaknessCWEID = ""
    
    try:
      reportScopeAssetType                = jsonResponse['data'][key]['relationships']['structured_scope']['data']['attributes']['asset_type']                 
    except Exception as e: 
      reportScopeAssetType = ""
    
    try:
      reportScopeAssetIdentifier          = jsonResponse['data'][key]['relationships']['structured_scope']['data']['attributes']['asset_identifier']           
    except Exception as e: 
      reportScopeAssetIdentifier = ""

    try:
      tmpTotalBountyAwarded = 0.00

      for key2 in range(len(jsonResponse['data'][key]['relationships']['bounties']['data'])):
        tmpAwardedAmount                  = jsonResponse['data'][key]['relationships']['bounties']['data'][key2]['attributes']['awarded_amount']           
        tmpAwardedBonusAmount             = jsonResponse['data'][key]['relationships']['bounties']['data'][key2]['attributes']['awarded_bonus_amount']  
        
        tmpTotalBountyAwarded = float(tmpTotalBountyAwarded) + (float(tmpAwardedAmount) + float(tmpAwardedBonusAmount))

      reportBountyAwardedAmount = str(tmpTotalBountyAwarded)

    except Exception as e: 
      reportBountyAwardedAmount = ""

    # write row to db
    try:      
      sql = "exec UpsertData @reportId=?, \
                             @bbProgramId=?,\
                             @reportState=?,\
                             @reportCreatedDateTime=?, \
                             @reportVulnerabilityInformation=?, \
                             @reportTitle=?, \
                             @reportTriagedDateTime=?, \
                             @reportClosedDateTime=?, \
                             @reportLastReporterActivityDateTime=?, \
                             @reportFirstProgramActivityDateTime=?, \
                             @reportLastProgramActivityDateTime=?, \
                             @reportBountyAwardedDateTime=?, \
                             @reportBountyAwardedAmount=?, \
                             @reportSwagAwardedDateTime=?,\
                             @reportDisclosedDateTime=?, \
                             @reportLastPublicActivityDateTime=?, \
                             @reportLastActivityDateTime=?, \
                             @reportIssueTrackerUrl=?, \
                             @researcherUsername=?, \
                             @researcherName=?, \
                             @researcherReputation=?, \
                             @researcherSignal=?, \
                             @researcherImpact=?, \
                             @reportSeverityCVSSRating=?, \
                             @reportSeverityCVSSScore=?, \
                             @reportSeverityCVSSSComplexity=?, \
                             @reportSeverityCVSSSVector=?, \
                             @reportSeverityCVSSSAvailability=?, \
                             @reportSeverityCVSSConfidentiality=?, \
                             @reportSeverityCVSSIntegrity=?, \
                             @reportSeverityCVSSPrivileges=?, \
                             @reportSeverityCVSSUserInteraction=?, \
                             @reportSeverityCVSSScopeChange=?, \
                             @reportWeaknessName=?, \
                             @reportWeaknessCWEID=?, \
                             @reportScopeAssetType=?, \
                             @reportScopeAssetIdentifier=?, \
                             @reportCustomFieldSubTakeover=?, \
                             @reportCustomFieldIPaddress=?, \
                             @ipAddressCountry=?, \
                             @ipAddressCountryCode=?, \
                             @ipAddressCity=?, \
                             @ipAddressRegion=?, \
                             @ipAddressPostalCode=?, \
                             @ipAddressLatitude=?, \
                             @ipAddressLongitude=?"
      result = conCursor.execute(sql, \
                              reportId, \
                              program_name, \
                              reportState, \
                              reportCreatedDateTime, \
                              reportVulnerabilityInformation, \
                              reportTitle, \
                              reportTriagedDateTime, \
                              reportClosedDateTime, \
                              reportLastReporterActivityDateTime, \
                              reportFirstProgramActivityDateTime, \
                              reportLastProgramActivityDateTime, \
                              reportBountyAwardedDateTime, \
                              reportBountyAwardedAmount, \
                              reportSwagAwardedDateTime, \
                              reportDisclosedDateTime, \
                              reportLastPublicActivityDateTime, \
                              reportLastActivityDateTime, \
                              reportIssueTrackerUrl, \
                              researcherUsername, \
                              researcherName, \
                              researcherReputation, \
                              researcherSignal, \
                              researcherImpact, \
                              reportSeverityCVSSRating, \
                              reportSeverityCVSSScore, \
                              reportSeverityCVSSSComplexity, \
                              reportSeverityCVSSSVector, \
                              reportSeverityCVSSSAvailability, \
                              reportSeverityCVSSConfidentiality, \
                              reportSeverityCVSSIntegrity, \
                              reportSeverityCVSSPrivileges,\
                              reportSeverityCVSSUserInteraction, \
                              reportSeverityCVSSScopeChange, \
                              reportWeaknessName, \
                              reportWeaknessCWEID, \
                              reportScopeAssetType, \
                              reportScopeAssetIdentifier, \
                              reportCustomFieldSubTakeover, \
                              reportCustomFieldIPaddress, \
                              ipAddressCountry, \
                              ipAddressCountryCode, \
                              ipAddressCity, \
                              ipAddressRegion, \
                              ipAddressPostalCode, \
                              ipAddressLatitude, \
                              ipAddressLongitude)      
      conCursor.commit()
    except Exception as e:
      print(jsonResponse['data'][key])
      print("Error in processReports(): " + str(e))
      print("ResearcherUserName=" + researcherUsername)
      print("ResearcherName=" + researcherName)
      print("ResearcherNameJSON=" + jsonResponse['data'][key]['relationships']['reporter']['data']['attributes']['name'])
      exit()  


############################################################################################
# Main prog
############################################################################################
def run():

  print("")
  print("")
  print("-----------------------------------------------------------")
  print("---------------- Get HackerOne Reports Data ---------------")
  print("-----------------------------------------------------------")
  print("")
  time.sleep(.10)

  print("1")
  
  if len(sys.argv) < 5:
    print("Syntax: python3 getH1Reports.py <args>")
    print("")
    print("args:")
    print("\t<DB Conn str>")
    print("\t<H1 API Token Name>")
    print("\t<H1 API Token>")
    print("\t<H1 Program Name>")
    exit()

  print("2")

  try:
    print("3")

    # set up db connection
    conn = pyodbc.connect(sys.argv[1])
    conCursor = conn.cursor()
    print("4")
  except Exception as e:
    print("Error: Unable to connect to the database using the connection string provided. Please check arguments and try again.")
    print(str(e))
    exit()

  try:
    print("5")

    h1ApiTokenName = sys.argv[2]
    h1ApiToken = sys.argv[3]
    h1ProgramName = sys.argv[4] 

    cursor.hide()
    page_number = 1
    done = False
     
    while(not done):
      # get next page
      print("\rRetrieving Page " + str(page_number) + " from " + h1ProgramName + "...")
      time.sleep(.01)
      jsonResponse = getReports(h1ApiTokenName, h1ApiToken, h1ProgramName, 100, page_number)

      # if no data, break loop
      if(len(jsonResponse['data']) == 0): 
        done = True
      else:
        # process the data
        processReports(h1ProgramName, jsonResponse, conCursor)
        page_number = page_number + 1

    print("Done!")
  except Exception as e:
      print("Error in processReports: " + str(e))
      exit()

  cursor.show()

  exit(1337)

if __name__ == "__main__":
    run()