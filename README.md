# DF_Mapper
Before to start, install the required python modules by running the following command:
pip install -r requirements.txt

From DF or CCX export the configuration and get the following files:
  To get the Protected Objects configuration, extract protected_object_configuration.json
  To get the Security Templates configuration, extract policy-editor-backup.json

Once you have the files copy or move them as follows:
  protected_object_configuration.json into folder input_po
  extract policy-editor-backup.json into folder input_st

Execute the Python file by running the following command:
python DF_Config_Mapper

From the menu you can select the following options to get the following:

  1. Get CSV for Protected Objects configuration - To export a csv file with the Protected Objects configuration
  2. Get CSV for Security Template configuration - To export a csv file with the Security Templates configuration
  3. Get CSV for all the JSON files - To export the two csv files with the corresponding configurations at the same time.

The exported csv files will be stored into the ouptu folder.
