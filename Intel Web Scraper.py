import requests
from bs4 import BeautifulSoup
from termcolor import colored
import time
import os


def INTEL_PROC_SCRAPPER(weblink):
    r = requests.get(weblink)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")

    print(colored("Essentials\n", 'green')) # ESSENTIALS

    items_essentials_1 = soup.find_all("a", {"class":"ark-accessible-color hrefcolor"})
    print(colored("Product Collection: ", 'blue')  + items_essentials_1[0].text.replace("\n", "").replace(" ", ""))

    items_essentials_2 = soup.find_all("span", {"data-key":"MarketSegment"})
    print(colored("Vertical Segments: ", 'blue') + items_essentials_2[0].text.replace("\n", "").replace(" ", ""))
    
    item_product_number = soup.find_all("span", {"data-key":"ProcessorNumber"})
    print(colored("Processor Number: ", 'blue') + item_product_number[0].text.replace("\n", "").replace(" ", ""))

    # filemake = open("Intel_Processor_Info.txt", 'w', encoding="utf8")
    FUCKING_FILE_NAME = item_product_number[0].text.replace("\n", "").replace(" ", "")
    filemake = open(FUCKING_FILE_NAME + ".txt", 'w', encoding="utf8")
    filemake.write("")
    filemake.close()

    # file = open("Intel_Processor_Info.txt", 'r+', encoding="utf8")
    file = open(FUCKING_FILE_NAME + ".txt", 'r+', encoding="utf8")
    file.write("ESSENTIALS - ")
    file.write("\nProduct Collection: " + str(items_essentials_1[0].text).replace("\n", "").replace(" ", ""))
    file.write("\nVertical Segments: " + str(items_essentials_2[0].text).replace("\n", "").replace(" ", ""))
    file.write("\nProcessor Number: " + str(item_product_number[0].text).replace("\n", "").replace(" ", ""))

    try: 
        item_offroad_map = soup.find_all("span", {"data-key":"OffRoadmap"})
        print(colored("Off Roadmap: ", 'blue') + item_offroad_map[0].text.replace("\n", "").replace(" ", ""))
        file.write("\nOff Roadmap: " + item_offroad_map[0].text.replace("\n", "").replace(" ", ""))
    except:
        print(colored("Unable to get Code Name\n", 'red'))
        file.write("\nUnable to get Code Name")

    try:
        item_code_name = soup.find_all("span", {"data-key":"CodeNameText"})
        print(colored("Code Name: ", 'blue') + item_code_name[0].find('a').text.replace("\n", "").replace(" ", ""))
        file.write("\nCode Name: " + item_code_name[0].text.replace("\n", "").replace(" ", ""))
    except:
        print(colored("Unable to get Code Name\n", 'red'))
        file.write("\nUnable to get Code Name")
    
    try:
        item_code_name_link = soup.find_all("span", {"data-key":"CodeNameText"})
        print(colored("Code Name Link: ", 'blue') + "https://ark.intel.com/" + item_code_name_link[0].find('a').get('href'))
        file.write("\nCode Name Link: " + "https://ark.intel.com/" + item_code_name_link[0].find('a').get('href'))
    except:
        print(colored("Unable to get Code Name Link\n", 'red'))
        file.write("\nUnable to get Code Name Link")
    
    try:
        item_launch_date = soup.find_all("span", {"data-key":"LaunchDate"})
        print(colored("Publication Date: ", 'blue') + item_launch_date[0].text.replace("\n", "").replace(""))
        file.write("\n Publication Date: " + item_launch_date[0].text.replace("\n", "").replace(""))
    except:
        print(colored("Unable to get Publication Date!\n", 'red'))
        file.write("\nUnable to get Publication Date!")
    
    try:
        item_status = soup.find_all("span", {"data-key":"StatusCodeText"})
        print(colored("Status: ", 'blue') + item_status[0].text.replace("\n", "").replace(" ", ""))
        file.write("\nStatus: " + item_status[0].text.replace("\n", "").replace(" ", ""))
    except:
        print(colored("Unable to get Status!\n", 'red'))
        file.write("\nUnable to get Status!")

    try:
        item_launch_date = soup.find_all("span", {"data-key":"BornOnDate"})
        print(colored("Launch Date: ", 'blue') + item_launch_date[0].text.replace("\n", "").replace(" ", ""))
        file.write("\nLaunch Date: " + item_launch_date[0].text.replace("\n", "").replace(" ", ""))
    except:
        print(colored("Unable to get Launch Date!\n", 'red'))
        file.write("\nUnable to get Launch Date!")

    try:
        item_expected_disconueance = soup.find_all("span", {"data-key":"ExpectedDiscontinuanceDate"})
        print(colored("Expected Discontinuance: ", 'blue') + item_expected_disconueance[0].text.replace("\n", "").replace(" ", ""))
        file.write("\nExpected Discontinuance: " + item_expected_disconueance[0].text.replace("\n", "").replace(" ", ""))
    except:
        print(colored("Unable to get Expected Discontinuance\n", 'red'))
        file.write("\nUnable to get Expected Discontinuance")

    try:
        item_lithography = soup.find_all("span", {"data-key":"Lithography"})
        print(colored("Lithography: ", 'blue') + item_lithography[0].text.replace("\n", "").replace(" ", ""))
        file.write("\nLithography: " + item_lithography[0].text.replace("\n", "").replace(" ", ""))
    except:
        print(colored("Unable to get Lithography!\n", 'red'))
        file.write("\nUnable to get Lithography!")

    print(colored("\n\nCPU Specifications\n", 'green')) # CPU SPECIFICATIONS
    file.write("\n\nCPU SPECIFICATIONS - ")

    try:
        item_core_count = soup.find_all("span", {"data-key":"CoreCount"})
        print(colored("Core Count: ", 'blue') + item_core_count[0].text.replace("\n", "").replace(" ", ""))
        file.write("\nCore Count: " + item_core_count[0].text.replace("\n", "").replace(" ", ""))
    except:
        print(colored("Unable to get Core Count!\n", 'red'))
        file.write("\nUnable to get Core Count!")

    try:
        item_thred_count = soup.find_all("span", {"data-key":"ThreadCount"})
        print(colored("Thread Count: ", 'blue') + item_thred_count[0].text.replace("\n", "").replace(" ", ""))
        file.write("\nThread Count: " + item_thred_count[0].text.replace("\n", "").replace(" ", ""))
    except:
        print(colored("Unable to get Thread Count!\n", 'red'))
        file.write("\nUnable to get Thread Count!")

    try:
        item_proc_base_freq = soup.find_all("span", {"data-key":"ClockSpeed"})
        print(colored("Processor Base Frequency: ", 'blue') + item_proc_base_freq[0].text.replace("\n", "").replace(" ", ""))
        file.write("\nProcessor Base Frequency: " + item_proc_base_freq[0].text.replace("\n", "").replace(" ", ""))
    except:
        print(colored("Unable to get Processor Base Frequency!\n", 'red'))
        file.write("\nUnable to get Processor Base Frequency!")

    try:
        item_proc_turbo_freq = soup.find_all("span", {"data-key":"ClockSpeedMax"})
        print(colored("Max Turbo Frequency: ", 'blue') + item_proc_turbo_freq[0].text.replace("\n", "").replace(" ", ""))
        file.write("\nMax Turbo Frequency: " + item_proc_turbo_freq[0].text.replace("\n", "").replace(" ", ""))
    except:
        print(colored("Unable to get Max Turbo Frequency!\n", 'red'))
        file.write("\nUnable to get Max Turbo Frequency!")

    try:
        item_cache = soup.find_all("span", {"data-key":"Cache"})
        print(colored("Cache: ", 'blue') + item_cache[0].text.replace("\n", "").replace(" ", ""))
        file.write("\nCache: " + item_cache[0].text.replace("\n", "").replace(" ", ""))
    except:
        print(colored("Unable to get Cache!\n", 'red'))
        file.write("\nUnable to get Cache!")

    try:
        item_bus_speed = soup.find_all("span", {"data-key":"Bus"})
        print(colored("Bus Speed: ", 'blue') + item_bus_speed[0].text.replace("\n", "").replace(" ", ""))
        file.write("\nBus Speed: " + item_bus_speed[0].text.replace("\n", "").replace(" ", ""))
    except:
        print(colored("Unable to get Bus Speed!\n", 'red'))
        file.write("\nUnable to get Bus Speed!")

    try:
        item_turbo_two_speed = soup.find_all("span", {"data-key":"TurboBoostTech2MaxFreq"})
        print(colored("Intel® Turbo Boost Technology 2.0 Frequency‡: ", 'blue') + item_turbo_two_speed[0].text.replace("\n", "").replace(" ", ""))
        file.write("\nIntel® Turbo Boost Technology 2.0 Frequency‡: " + item_turbo_two_speed[0].text.replace("\n", "").replace(" ", ""))
    except:
        print(colored("Unable to get Intel® Turbo Boost Technology 2.0 Frequency‡ \n", 'red'))
        file.write("\nUnable to get Intel® Turbo Boost Technology 2.0 Frequency‡!")
    
    try:
        item_turbo_three_speed = soup.find_all("span", {"data-key":"TurboBoostMaxTechMaxFreq"})
        print(colored("Intel® Turbo Boost Technology 3.0 Frequency‡: ", 'blue') + item_turbo_three_speed[0].text.replace("\n", "").replace(" ", ""))
        file.write("\nIntel® Turbo Boost Technology 3.0 Frequency‡: " + item_turbo_three_speed[0].text.replace("\n", "").replace(" ", ""))
    except:
        print(colored("Unable to get Intel® Turbo Boost Technology 3.0 Frequency‡ \n", 'red'))
        file.write("\nUnable to get Intel® Turbo Boost Technology 3.0 Frequency‡!")

    try:
        item_tdp = soup.find_all("span", {"data-key":"MaxTDP"})
        print(colored("TDP: ", 'blue') + item_tdp[0].text.replace("\n", "").replace(" ", ""))
        file.write("TDP: " + item_tdp[0].text.replace("\n", "").replace(" ", ""))
    except:
        print(colored("Unable to get TDP!\n", 'red'))
        file.write("\nUnable to get TDP!")
    
    try:
        item_tdp_configrbl_down_freq = soup.find_all("span", {"data-key":"ConfigTDPMinFrequency"})
        print(colored("Configurable TDP-down Frequency: ", 'blue') + item_tdp_configrbl_down_freq[0].text.replace("\n", "").replace(" ", ""))
        file.write("Configurable TDP-down Frequency: " + item_tdp_configrbl_down_freq[0].text.replace("\n", "").replace(" ", ""))
    except:
        print(colored("Unable to get Configurable TDP-down Frequency!\n", 'red'))
        file.write("\nUnable to get Configurable TDP-down Frequency!")
    
    try:
        item_tdp_cinfgrbl_down = soup.find_all("span", {"data-key":"MaxTDP"})
        print(colored("Configurable TDP-down: ", 'blue') + item_tdp_cinfgrbl_down[0].text.replace("\n", "").replace(" ", ""))
        file.write("Configurable TDP-down: " + item_tdp_cinfgrbl_down[0].text.replace("\n", "").replace(" ", ""))
    except:
        print(colored("Unable to get Configurable TDP-down!\n", 'red'))
        file.write("\nUnable to get Configurable TDP-down!")

    try:
        print(colored("\n\nSupplemental Information\n", 'green')) # SUPPLEMENTAL INFORMATION
        file.write("\n\nSUPPLEMENTAL INFORMATION -")
        
        try:
            item_emb_options_available = soup.find_all("span", {"data-key":"Embedded"})
            print(colored("Embedded Options Available: ", 'blue') + item_emb_options_available[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nEmbedded Options Available: " + item_emb_options_available[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Embedded Options Available! \n", 'red'))
            file.write("\nUnable to get Embedded Options Available!")

        try:
            item_datasheet = soup.find_all("a", {"class":"ark-accessible-color hrefcolor"})
            print(colored("Datasheet: ", 'blue') + item_datasheet[0].text.text.replace("\n", "").replace(" ", ""))
            file.write("\nDatasheet: " + item_datasheet[0].text.text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Datasheet\n", 'red'))
            file.write("\nUnable to get Datasheet")
        
        try:
            print(colored("Datasheet Link: ", 'blue') + "https://ark.intel.com" + item_datasheet[0].get('href'))
            file.write("\nDatasheet Link: " + "https://ark.intel.com" + item_datasheet[0].get('href'))
        except:
            print(colored("Unable to get Datasheet Link\n", 'red'))
            file.write("\nUnable to ge Datsheet Link! ")
    except:
        print(colored("No Supplemental Information\n", 'red'))
        file.write("\nNo Supplemental Information")
    
    print(colored("\n\nMemory Specifications\n", 'green')) # MEMORY SPECIFICATIONS
    file.write("\n\nMEMORY SPECIFICATIONS -")

    try:
        item_proc_graphics = soup.find_all("span", {"data-key":"MaxMem"})
        print(colored("Max Memory Size (dependent on memory type): ", 'blue') + item_proc_graphics[0].text.replace("\n", "").replace(" ", ""))
        file.write("\nMax Memory Size (dependent on memory type): " + item_proc_graphics[0].text.replace("\n", "").replace(" ", ""))
    except:
        print(colored("Unable to get Max Memory Size (dependent on memory type)!\n", 'red'))
        file.write("\nUnable to get Max Memory Size (dependent on memory type)!")

    try:
        item_mem_types = soup.find_all("span", {"data-key":"MemoryTypes"})
        print(colored("Memory Types: ", 'blue') + item_mem_types[0].text.replace("\n", "").replace(" ", ""))
        file.write("\nMemory Types: " + item_mem_types[0].text.replace("\n", "").replace(" ", ""))
    except:
        print(colored("Unable to get Memory Types!\n", 'red'))
        file.write("\nUnable to get Memory Types!")

    try:
        item_max_mem_channels = soup.find_all("span", {"data-key":"NumMemoryChannels"})
        print(colored("Max # of Memory Channels: ", 'blue') + item_max_mem_channels[0].text.replace("\n", "").replace(" ", ""))
        file.write("\nMax # of Memory Channels: " + item_max_mem_channels[0].text.replace("\n", "").replace(" ", ""))
    except:
        print(colored("Unable to get Max # of Memory Channels!\n", 'red'))
        file.write("\nUnable to get Max # of Memory Channels!")

    try:
        item_max_mem_bandwidth = soup.find_all("span", {"data-key":"MaxMemoryBandwidth"})
        print(colored("Max Memory Bandwidth: ", 'blue') + item_max_mem_bandwidth[0].text.replace("\n", "").replace(" ", ""))
        file.write("\nMax Memory Bandwidth: " + item_max_mem_bandwidth[0].text.replace("\n", "").replace(" ", ""))
    except:
        print(colored("Unable to get Max Memory Bandwidth!\n", 'red'))
        file.write("\nUnable to get Max Memory Bandwidth!")

    try:
        item_max_ecc_mem_supt = soup.find_all("span", {"data-key":"ECCMemory"})
        print(colored("ECC Memory Supported ‡: ", 'blue') + item_max_ecc_mem_supt[0].text.replace("\n", "").replace(" ", ""))
        file.write("\nECC Memory Supported ‡: " + item_max_ecc_mem_supt[0].text.replace("\n", "").replace(" ", ""))
    except:
        print(colored("Unable to get ECC Memory Supported!\n", 'red'))
        file.write("\nUnable to get ECC Memory Supported!")


    try:
        print(colored("\n\nProcessor Graphics\n", 'green')) # Processor Graphics
        file.write("\n\nPROCESSOR GRAPHICS -")

        try:
            item_graphics_processor = soup.find_all("span", {"data-key":"ProcessorGraphicsModelId"})
            print(colored("Processor Graphics: ", 'blue') + item_graphics_processor[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nProcessor Graphics: " + item_graphics_processor[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Processor Graphics! \n", 'red'))
            file.write("\nUnable to get Processor Graphics!")

        try:
            item_graphice_base_freq = soup.find_all("span", {"data-key":"GraphicsFreq"})
            print(colored("Graphics Base Frequency: ", 'blue') + item_graphice_base_freq[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nGraphics Base Frequency: " + item_graphice_base_freq[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Graphics Base Frequency! \n", 'red'))
            file.write("\nUnable to get Graphics Base Frequency!")

        try:
            item_max_dynamic_freq = soup.find_all("span", {"data-key":"GraphicsMaxFreq"})
            print(colored("Graphics Max Dynamic Frequency: ", 'blue') + item_max_dynamic_freq[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nGraphics Max Dynamic Frequency: " + item_max_dynamic_freq[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Graphics Max Dynamic Frequency! \n", 'red'))
            file.write("\nUnable to get Graphics Max Dynamic Frequency!")
        
        try:
            item_max_video_mem = soup.find_all("span", {"data-key":"GraphicsMaxMem"})
            print(colored("Graphics Video Max Memory: ", 'blue') + item_max_video_mem[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nGraphics Video Max Memory: " + item_max_video_mem[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Graphics Video Max Memory! \n", 'red'))
            file.write("\nUnable to get Graphics Video Max Memory!")

        try:
            item_vide_output_graphics = soup.find_all("span", {"data-key":"GraphicsOutput"})
            print(colored("Graphics Output: ", 'blue') + item_vide_output_graphics[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nGraphics Output: " + item_vide_output_graphics[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Graphics Output! \n", 'red'))
            file.write("\nUnable to get Graphics Output!")
        
        try:
            item_gpu_excecution_units = soup.find_all("span", {"data-key":"GraphicsExecutionUnits"})
            print(colored("Execution Units: ", 'blue') + item_gpu_excecution_units[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nExecution Units: " + item_gpu_excecution_units[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Execution Units! \n", 'red'))
            file.write("\nUnable to get Execution Units!")

        try:
            item_gpu_hdmi = soup.find_all("span", {"data-key":"GraphicsMaxResolutionHDMI"})
            print(colored("Max Resolution (HDMI): ", 'blue') + item_gpu_hdmi[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nMax Resolution (HDMI): " + item_gpu_hdmi[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Max Resolution (HDMI)! \n", 'red'))
            file.write("\nUnable to get Max Resolution (HDMI)!")
        
        try:
            item_gpu_dp = soup.find_all("span", {"data-key":"GraphicsMaxResolutionDP"})
            print(colored("Max Resolution (DP): ", 'blue') + item_gpu_dp[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nMax Resolution (DP): " + item_gpu_dp[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Max Resolution (DP)! \n", 'red'))
            file.write("\nUnable to get Max Resolution (DP)!")
        
        try:
            item_gpu_edp = soup.find_all("span", {"data-key":"GraphicsMaxResolutionIFP"})
            print(colored("Max Resolution (eDP - Integrated Flat Panel): ", 'blue') + item_gpu_edp[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nMax Resolution (eDP - Integrated Flat Panel): " + item_gpu_edp[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Max Resolution (eDP - Integrated Flat Panel)! \n", 'red'))
            file.write("\nUnable to get Max Resolution (eDP - Integrated Flat Panel)!")
        
        try:
            item_gpu_vga = soup.find_all("span", {"data-key":"GraphicsMaxResoluionVGA"})
            print(colored("Max Resolution (VGA): ", 'blue') + item_gpu_vga[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nMax Resolution (VGA): "+ item_gpu_vga[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Max Resolution (VGA)! \n", 'red'))
            file.write("\nUnable to get Max Resolution (VGA)!")

        try:
            item_directx = soup.find_all("span", {"data-key":"GraphicsDirectXSupport"})
            print(colored("DirectX* Support: ", 'blue') + item_directx[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nDirectX* Support: " + item_directx[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get DirectX* Support! \n", 'red'))
            file.write("\nUnable to get DirectX* Support!")
        
        try:
            item_opengl = soup.find_all("span", {"data-key":"GraphicsOpenGLSupport"})
            print(colored("OpenGL* Support: ", 'blue') + item_opengl[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nOpenGL* Support: " + item_opengl[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get OpenGL* Support! \n", 'red'))
            file.write("\nUnable to get OpenGL* Support!")
        
        try:
            item_intel_quicksyncvid = soup.find_all("span", {"data-key":"QuickSyncVideo"})
            print(colored("Intel® Quick Sync Video: ", 'blue') + item_intel_quicksyncvid[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® Quick Sync Video: " + item_intel_quicksyncvid[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® Quick Sync Video! \n", 'red'))
            file.write("\nUnable to get Intel® Quick Sync Video!")
        
        try:
            item_intel_tru3dtech = soup.find_all("span", {"data-key":"InTru3D"})
            print(colored("Intel® InTru™ 3D Technology: ", 'blue') + item_intel_tru3dtech[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® InTru™ 3D Technology: " + item_intel_tru3dtech[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® InTru™ 3D Technology! \n", 'red'))
            file.write("\nUnable to get Intel® InTru™ 3D Technology!")
        
        try:
            item_fdi_intel = soup.find_all("span", {"data-key":"FDI"})
            print(colored("Intel® Flexible Display Interface (Intel® FDI): ", 'blue') + item_fdi_intel[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® Flexible Display Interface (Intel® FDI): " + item_fdi_intel[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® Flexible Display Interface (Intel® FDI)! \n", 'red'))
            file.write("\nUnable to get Intel® Flexible Display Interface (Intel® FDI)!")
        
        try:
            item_CVHDtech = soup.find_all("span", {"data-key":"CVTHD"})
            print(colored("Intel® Clear Video HD Technology: ", 'blue') + item_CVHDtech[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® Clear Video HD Technology: " + item_CVHDtech[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® Clear Video HD Technology! \n", 'red'))
            file.write("\nUnable to get Intel® Clear Video HD Technology!")
        
        try:
            item_CVHDtech = soup.find_all("span", {"data-key":"NumDisplaysSupported"})
            print(colored("# of Displays Supported: ", 'blue') + item_CVHDtech[0].text.replace("\n", "").replace(" ", ""))
            file.write("\n# of Displays Supported: " + item_CVHDtech[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get # of Displays Supported! \n", 'red'))
            file.write("\nUnable to get # of Displays Supported!")
        
        try:
            item_device_id = soup.find_all("span", {"data-key":"GraphicsDeviceId"})
            print(colored("Device ID: ", 'blue') + item_device_id[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nDevice ID: " + item_device_id[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Device ID! \n", 'red'))
            file.write("\nUnable to get Device ID!")
        
        try:
            item_device_openclsupt = soup.find_all("span", {"data-key":"GraphicsOpenCLSupport"})
            print(colored("OpenCL* Support: ", 'blue') + item_device_openclsupt[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nOpenCL* Support: " + item_device_openclsupt[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get OpenCL* Support! \n", 'red'))
            file.write("\nUnable to get OpenCL* Support!")
    
    except:
        print(colored("No Processor Graphics Information\n", 'red'))
        file.write("\nNo Processor Graphics Information")

    try:
        print(colored("\n\nExpansion Options\n", 'green')) # Expansion Options
        file.write("\n\nEXPANSION OPTIONS - ")
        try:
            item_exp_scalbility = soup.find_all("span", {"data-key":"ScalableSockets"})
            print(colored("Scalability: ", 'blue') + item_exp_scalbility[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nScalability: " + item_exp_scalbility[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Scalability! \n", 'red'))
            file.write("\nUnable to get Scalability!")

        try:
            item_exp_pxierev = soup.find_all("span", {"data-key":"PCIExpressRevision"})
            print(colored("PCI Express Revision: ", 'blue') + item_exp_pxierev[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nPCI Express Revision: " + item_exp_pxierev[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get PCI Express Revision! \n", 'red'))   
            file.write("\nUnable to get PCI Express Revision!")
        
        try:
            item_exp_pcieconfigs = soup.find_all("span", {"data-key":"PCIExpressConfigs"})
            print(colored("PCI Express Configurations: ", 'blue') + item_exp_pcieconfigs[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nPCI Express Configurations: " + item_exp_pcieconfigs[0].text.replace("\n", "").replace(" ", ""))

        except:
            print(colored("Unable to get PCI Express Configurations! \n", 'red'))
            file.write("\nUnable to get PCI Express Configurations! ")
        
        try:
            item_exp_scalbility = soup.find_all("span", {"data-key":"NumPCIExpressPorts"})
            print(colored("Max # of PCI Express Lanes: ", 'blue') + item_exp_scalbility[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nMax # of PCI Express Lanes: " + item_exp_scalbility[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Max # of PCI Express Lanes! \n", 'red'))
            file.write("\nUnable to get Max # of PCI Express Lanes!")
    except:
        print(colored("No Expansion Options Information\n", 'red'))
        file.write("\nUnable to get Status!")
    
    try:
        print(colored("\n\nPackage Specifications\n", 'green')) # Package Specifications
        file.write("\n\nPACKAGE SPECIFICATIONS - ")
        try:
            item_cpu_sock = soup.find_all("span", {"data-key":"SocketsSupported"})
            print(colored("Sockets Supported: ", 'blue') + item_cpu_sock[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nSockets Supported: " + item_cpu_sock[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Sockets Supported! \n", 'red'))
            file.write("\nUnable to get Sockets Supported!")
        
        try:
            item_cpu_max_no = soup.find_all("span", {"data-key":"MaxCPUs"})
            print(colored("Max CPU Configuration: ", 'blue') + item_cpu_max_no[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nMax CPU Configuration: " + item_cpu_max_no[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Max CPU Configuration! \n", 'red'))
            file.write("\nUnable to get Status!")

        try:
            item_thermal_solution_spec = soup.find_all("span", {"data-key":"ThermalSolutionSpecification"})
            print(colored("Thermal Solution Specification: ", 'blue') + item_thermal_solution_spec[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nThermal Solution Specification: " + item_thermal_solution_spec[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Thermal Solution Specification! \n", 'red'))
            file.write("\nUnable to get Thermal Solution Specification!")
        
        try:
            item_tcase_temp = soup.find_all("span", {"data-key":"TCase"})
            print(colored("TCASE: ", 'blue') + item_tcase_temp[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nTCASE: " + item_tcase_temp[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get TCASE! ", 'red'))
            file.write("\nUnable to get TCASE!")
        
        try:
            item_tjunc_temp = soup.find_all("span", {"data-key":"ThermalJunctionRateCode"})
            print(colored("TJUNCTION: ", 'blue') + item_tjunc_temp[0].text.replace("\n", "").replace(" ", ""))
            file.write("\TJUNCTION: " + item_tjunc_temp[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get TJUNCTION! ", 'red'))
            file.write("\nUnable to get TJUNCTION!")
            
        try:
            item_exp_scalbility = soup.find_all("span", {"data-key":"PackageSize"})
            print(colored("Package Size: ", 'blue') + item_exp_scalbility[0].text.replace("\n", "").replace(" ", ""))
            file.write("Package Size: " + item_exp_scalbility[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Package Size! ", 'red'))
            file.write("\nUnable to get Package Size!")
    except:
        print(colored("No Expansion Options Information", 'red'))
        file.write("\nNo Expansion Options Information")
    
    try:
        print(colored("\n\nAdvanced Technologies\n", 'green')) # Advanced Technologies
        file.write("\n\nAdvanced Technologies")

        try:
            item_dl_boost = soup.find_all("span", {"data-key":"DeepLearningBoostVersion"})
            print(colored("Intel® Deep Learning Boost (Intel® DL Boost): ", 'blue') + item_dl_boost[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® Deep Learning Boost (Intel® DL Boost): " + item_dl_boost[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® Deep Learning Boost (Intel® DL Boost)! \n", 'red'))
            file.write("\nUnable to get Intel® Deep Learning Boost (Intel® DL Boost)!")

        try:
            item_optane_mem_supt = soup.find_all("span", {"data-key":"OptaneMemorySupport"})
            print(colored("Intel® Optane™ Memory Supported: ", 'blue') + item_optane_mem_supt[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® Optane™ Memory Supported: " + item_optane_mem_supt[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® Optane™ Memory Supported! \n", 'red'))
            file.write("\nUnable to get Intel® Optane™ Memory Supported!")

        try:
            item_turbo_boost_tv = soup.find_all("span", {"data-key":"ThermalVelocityBoostVersion"})
            print(colored("Intel® Thermal Velocity Boost: ", 'blue') + item_turbo_boost_tv[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® Thermal Velocity Boost: " + item_turbo_boost_tv[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® Thermal Velocity Boost! \n", 'red'))
            file.write("\nUnable to get Intel® Thermal Velocity Boost!")
        
        try:
            item_turbo_boost_tv_max_3 = soup.find_all("span", {"data-key":"TurboBoostMaxTechVersion"})
            print(colored("Intel® Turbo Boost Technology: ", 'blue') + item_turbo_boost_tv_max_3[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® Turbo Boost Technology: " + item_turbo_boost_tv_max_3[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® Turbo Boost Technology! \n", 'red'))
            file.write("\nUnable to get Intel® Turbo Boost Technology!")

        try:
            item_turbo_boost_tv = soup.find_all("span", {"data-key":"TBTVersion"})
            print(colored("Intel® Turbo Boost Technology: ", 'blue') + item_turbo_boost_tv[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® Turbo Boost Technology: " + item_turbo_boost_tv[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® Turbo Boost Technology! \n", 'red'))
            file.write("\nUnable to get Intel® Turbo Boost Technology!")
        

        try:
            item_v_pro_playformEligibility = soup.find_all("span", {"data-key":"VProTechnology"})
            print(colored("Intel vPro® Platform Eligibility: ", 'blue') + item_v_pro_playformEligibility[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel vPro® Platform Eligibility: " + item_v_pro_playformEligibility[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel vPro® Platform Eligibility! \n", 'red'))
            file.write("\nUnable to get Intel vPro® Platform Eligibility!")
        
        try:
            item_hyperthreading_tech = soup.find_all("span", {"data-key":"HyperThreading"})
            print(colored("Intel® Hyper-Threading Technology: ", 'blue') + item_hyperthreading_tech[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® Hyper-Threading Technology: " + item_hyperthreading_tech[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® Hyper-Threading Technology! \n", 'red'))
            file.write("\nUnable to get Intel® Hyper-Threading Technology!")
        
        try:
            item_vtx_one = soup.find_all("span", {"data-key":"VTX"})
            print(colored("Intel® Virtualization Technology (VT-x): ", 'blue') + item_vtx_one[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® Virtualization Technology (VT-x): " + item_vtx_one[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® Virtualization Technology (VT-x)! \n", 'red'))
            file.write("\nUnable to get Intel® Virtualization Technology (VT-x)!")
        
        try:
            item_vtd = soup.find_all("span", {"data-key":"VTD"})
            print(colored("Intel® Virtualization Technology for Directed I/O (VT-d): ", 'blue') + item_vtd[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® Virtualization Technology for Directed I/O (VT-d): " + item_vtd[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® Virtualization Technology for Directed I/O (VT-d)! \n", 'red'))
            file.write("\nUnable to get Intel® Virtualization Technology for Directed I/O (VT-d)!")
        
        try:
            item_ept = soup.find_all("span", {"data-key":"ExtendedPageTables"})
            print(colored("Intel® VT-x with Extended Page Tables (EPT): ", 'blue') + item_ept[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® VT-x with Extended Page Tables (EPT): " + item_ept[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® VT-x with Extended Page Tables (EPT)! \n", 'red'))
            file.write("\nUnable to get Status!")
        
        try:
            item_sync_extension = soup.find_all("span", {"data-key":"TransactionalSynchronizationExtensionVersion"})
            print(colored("Intel® Transactional Synchronization Extensions: ", 'blue') + item_sync_extension[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® Transactional Synchronization Extensions: " + item_sync_extension[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® Transactional Synchronization Extensions! \n", 'red'))
            file.write("\nUnable to get Intel® Transactional Synchronization Extensions!")

        try:
            item_intel64thing = soup.find_all("span", {"data-key":"EM64"})
            print(colored("Intel® 64: ", 'blue') + item_intel64thing[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® 64: " + item_intel64thing[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® 64! \n", 'red'))
            file.write("\nUnable to get Intel® 64!")
        
        try:
            item_instruction_set = soup.find_all("span", {"data-key":"InstructionSet"})
            print(colored("Instruction Set: ", 'blue') + item_instruction_set[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nInstruction Set: " + item_instruction_set[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Instruction Set! \n", 'red'))
            file.write("\nUnable to get Instruction Set!")
        
        try:
            item_instr_set_extensions = soup.find_all("span", {"data-key":"InstructionSetExtensions"})
            print(colored("Instruction Set Extensions: ", 'blue') + item_instr_set_extensions[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nInstruction Set Extensions: " + item_instr_set_extensions[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Instruction Set Extensions! \n", 'red'))
            file.write("\nUnable to get Instruction Set Extensions!")
        
        try:
            item_imy_wifi_tech = soup.find_all("span", {"data-key":"MyWiFiTech"})
            print(colored("Intel® My WiFi Technology: ", 'blue') + item_imy_wifi_tech[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® My WiFi Technology: " + item_imy_wifi_tech[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® My WiFi Technology! \n", 'red'))
            file.write("\nUnable to get Intel® My WiFi Technology!")

        try:
            item_idle_states = soup.find_all("span", {"data-key":"HaltState"})
            print(colored("Idle States: ", 'blue') + item_idle_states[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIdle States: " + item_idle_states[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Idle States! \n", 'red'))
            file.write("\nUnable to get Idle States!")
        
        try:
            item_speedstep_tech_intel = soup.find_all("span", {"data-key":"SpeedstepTechnology"})
            print(colored("Enhanced Intel SpeedStep® Technology: ", 'blue') + item_speedstep_tech_intel[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nEnhanced Intel SpeedStep® Technology: " + item_speedstep_tech_intel[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Enhanced Intel SpeedStep® Technology! \n", 'red'))
            file.write("\nUnable to get Enhanced Intel SpeedStep® Technology!")
        
        try:
            item_thermal_monitorying_tech = soup.find_all("span", {"data-key":"ThermalMonitoring2Indicator"})
            print(colored("Thermal Monitoring Technologies: ", 'blue') + item_thermal_monitorying_tech[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nThermal Monitoring Technologies: " + item_thermal_monitorying_tech[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Thermal Monitoring Technologies! \n", 'red'))
            file.write("\nUnable to get Thermal Monitoring Technologies!")
        
        # idk how this came here
        # try:
        #     item_scalability_thing = soup.find_all("span", {"data-key":"IdentityProtectionTechVersion"})
        #     print(colored("Scalability: ", 'blue') + item_scalability_thing[0].text.replace("\n", "").replace(" ", ""))
        #     file.write("\nScalability: " + item_scalability_thing[0].text.replace("\n", "").replace(" ", ""))
        # except:
        #     print(colored("Unable to get Scalability! \n", 'red'))
        #     file.write("\nUnable to get Scalability!")
        
        try:
            item_iIdentity_protection = soup.find_all("span", {"data-key":"IdentityProtectionTechVersion"})
            print(colored("Intel® Identity Protection Technology: ", 'blue') + item_iIdentity_protection[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® Identity Protection Technology: " + item_iIdentity_protection[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® Identity Protection Technology! \n", 'red'))
            file.write("\nUnable to get Intel® Identity Protection Technology!")
        
        try:
            item_stable_img_platform_programSIPP = soup.find_all("span", {"data-key":"StableImagePlatformProgramVersion"})
            print(colored("Intel® Stable Image Platform Program (SIPP): ", 'blue') + item_stable_img_platform_programSIPP[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® Stable Image Platform Program (SIPP): " + item_stable_img_platform_programSIPP[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® Stable Image Platform Program (SIPP)! ", 'red'))
            file.write("\nUnable to get Intel® Stable Image Platform Program (SIPP)!")

        try:
            item_guassian_neural_accelerator = soup.find_all("span", {"data-key":"IntelGaussianandNeuralAccelerator"})
            print(colored("Intel® Gaussian and Neural Accelerator 2.0: ", 'blue') + item_guassian_neural_accelerator[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® Gaussian and Neural Accelerator 2.0: " + item_guassian_neural_accelerator[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® Gaussian and Neural Accelerator 2.0! \n", 'red'))
            file.write("\nUnable to get Intel® Gaussian and Neural Accelerator 2.0!")
        
        try:
            item_guassian_neural_accelerator = soup.find_all("span", {"data-key":"DemandBasedSwitching"})
            print(colored("Intel® Demand Based Switching: ", 'blue') + item_guassian_neural_accelerator[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® Demand Based Switching: " + item_guassian_neural_accelerator[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® Demand Based Switching! \n", 'red'))
            file.write("\nUnable to get IIntel® Demand Based Switching!")

    except:
        print(colored("No Advanced Technologies Information", 'red'))
        file.write("\nNo Advanced Technologies Information")
    
    try:
        print(colored("\n\nSecurity & Reliability\n", 'green')) # Security & Reliability
        file.write("\n\nSECURITY & RELIABILITY")
        try:
            item_aesTech = soup.find_all("span", {"data-key":"AESTech"})
            print(colored("Intel® AES New Instructions: ", 'blue') + item_aesTech[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® AES New Instructions: " + item_aesTech[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® AES New Instructions! \n", 'red'))
            file.write("\nUnable to get Intel® AES New Instructions!")
        
        try:
            item_secure_keything = soup.find_all("span", {"data-key":"SecureKeyTechVersion"})
            print(colored("Secure Key: ", 'blue') + item_secure_keything[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nSecure Key: " + item_secure_keything[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Secure Key! \n", 'red'))
            file.write("\nUnable to get Secure Key!")
        
        try:
            item_ostechagurd_thing = soup.find_all("span", {"data-key":"OSGuardTechVersion"})
            print(colored("Intel® OS Guard: ", 'blue') + item_ostechagurd_thing[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® OS Guard: " + item_ostechagurd_thing[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® OS Guard! \n", 'red'))
            file.writefile.write("\nUnable to get Intel® OS Guard!")
        
        try:
            item_trusted_excec_intel = soup.find_all("span", {"data-key":"TXT"})
            print(colored("Intel® Trusted Execution Technology : ", 'blue') + item_trusted_excec_intel[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® Trusted Execution Technology : " + item_trusted_excec_intel[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® Trusted Execution Technology ! \n", 'red'))
            file.write("\nUnable to get Intel® Trusted Execution Technology!")
        
        try:
            item_excecute_disable = soup.find_all("span", {"data-key":"ExecuteDisable"})
            print(colored("Execute Disable Bit: ", 'blue') + item_excecute_disable[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nExecute Disable Bit: " + item_excecute_disable[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Execute Disable Bit! \n", 'red'))
            file.write("\nUnable to get Execute Disable Bit!")
        
        try:
            item_antitheft_tech = soup.find_all("span", {"data-key":"AntiTheftTechnology"})
            print(colored("Anti-Theft Technology: ", 'blue') + item_antitheft_tech[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nAnti-Theft Technology: " + item_antitheft_tech[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Anti-Theft Technology! \n", 'red'))
            file.write("\nUnable to get Anti-Theft Technology!")
        
        try:
            item_software_gaurd = soup.find_all("span", {"data-key":"SoftwareGuardExtensions"})
            print(colored("Intel® Software Guard Extensions (Intel® SGX): ", 'blue') + item_software_gaurd[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® Software Guard Extensions (Intel® SGX): " + item_software_gaurd[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® Software Guard Extensions (Intel® SGX)! \n", 'red'))
            file.write("\nUnable to get Intel® Software Guard Extensions (Intel® SGX)!")
        
        try:
            item_boot_gaurd = soup.find_all("span", {"data-key":"DeviceProtectionTechBootGuardVersion"})
            print(colored("Intel® Boot Guard: ", 'blue') + item_boot_gaurd[0].text.replace("\n", "").replace(" ", ""))
            file.write("\nIntel® Boot Guard: " + item_boot_gaurd[0].text.replace("\n", "").replace(" ", ""))
        except:
            print(colored("Unable to get Intel® Boot Guard! \n", 'red'))
            file.write("\nUnable to get Intel® Boot Guard!")
        
    except:
        print(colored("No Security & Reliability Information", 'red'))
        file.write("\nNo Security & Reliability Information")
    
    file.write("\n\nIntel Web Scraper by ZeaCeR#5641")
    file.close()

    print(colored("\nCOMPLETED! SAVED ALL THE RESULTS TO A FILE", 'green'))
    print(colored("PROGRAM WILL CLOSE IN 5 MINUTES!", 'green'))
    time.sleep(300)
    
try: 
    os.system('cls')
    weblink = input("+ Enter the website link: ")
    # weblink="https://ark.intel.com/content/www/us/en/ark/products/80810/intel-core-i5-4690-processor-6m-cache-up-to-3-90-ghz.html"
    INTEL_PROC_SCRAPPER(weblink)

except:
    os.system('cls')
    print(colored("- Something has gone wrong! Please contact the developer to fix this!\n- The program will be started again!", 'red'))
    time.sleep(5)
    os.system('cls')
    weblink = input("+ Enter the website link: ")
    # weblink="https://ark.intel.com/content/www/us/en/ark/products/80810/intel-core-i5-4690-processor-6m-cache-up-to-3-90-ghz.html"
    INTEL_PROC_SCRAPPER(weblink)