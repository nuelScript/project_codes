# Importing necessary functions from different modules
from ETHYLENE import read_ethylene, read_shared_data as read_ethylene_shared_data
from ETHANOL import  read_ethanol, read_shared_data as read_ethanol_shared_data
from DHT22_SENSOR import read_dht, read_shared_data as read_dht_shared_data
from GREEN_LED import on_LED as green_led_on
from AI_MODEL import make_prediction, get_grade
from RED_LED_and_BUZZER import check_and_trigger_devices
from BLYNK import handle_fruit_type, handle_num_fruits, update_shared_data as update_blynk_shared_data, update_blynk_with_grade

def main():
    # Step 1: Turn on the green LED
    green_led_on()
    
    # Step 2: Read and update DHT sensor data
    read_dht_shared_data()
    dht_data =read_dht()
    
    # Step 3: Read and update Ethanol data
    read_ethanol_shared_data()
    ethanol_data = read_ethanol()
    
    # Step 4: Read and update Ethylene data
    read_ethylene_shared_data()
    ethylene_data = read_ethylene()
    
    # Step 5: Handle fruit type and number of fruits, then update Blynk
    fruit_type = handle_fruit_type()
    num_fruits = handle_num_fruits()
    update_blynk_shared_data(fruit_type, num_fruits)
    
    # Step 6: Use the AI model to make predictions and get the grade
    prediction = make_prediction(dht_data, ethanol_data, ethylene_data, fruit_type, num_fruits)
    grade = get_grade(prediction)
    
    # Step 7: Update Blynk with the grade
    update_blynk_with_grade(grade)
    
    # Step 8: Pass the grade to RED_LED_and_BUZZER to check and trigger devices
    check_and_trigger_devices(grade)

# Ensure the script runs only when executed directly, not when imported as a module
if __name__ == "__main__":
    main()
