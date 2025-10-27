"""
Module de simulation Climate & Air Quality
Gère la température, humidité, CO₂ et contrôle de ventilation
"""

import random
import time
from config import CLIMATE_CONFIG


class ClimateModule:
    def __init__(self):
        self.temperature = 24.0
        self.humidity = 50.0
        self.co2 = 600
        self.ventilator_on = False
        self.forced_ventilation = False
        self.last_update = time.time()
        
        # Variables pour scénarios forcés
        self.scenario_active = False
        self.scenario_end_time = 0
        self.forced_temp = None
        self.forced_co2 = None
    
    def update_sensors(self):
        """Met à jour les valeurs des capteurs simulés"""
        current_time = time.time()
        
        # Vérifier si un scénario forcé est actif
        if self.scenario_active and current_time > self.scenario_end_time:
            self.scenario_active = False
            self.forced_temp = None
            self.forced_co2 = None
        
        # Générer valeurs aléatoires ou utiliser valeurs forcées
        if self.forced_temp is not None:
            self.temperature = self.forced_temp + random.uniform(-0.5, 0.5)
        else:
            # Variation normale de température
            temp_min, temp_max = CLIMATE_CONFIG['temp_range']
            self.temperature += random.uniform(-0.3, 0.3)
            self.temperature = max(temp_min, min(temp_max, self.temperature))
        
        if self.forced_co2 is not None:
            self.co2 = int(self.forced_co2 + random.uniform(-20, 20))
        else:
            # Variation normale de CO₂
            co2_min, co2_max = CLIMATE_CONFIG['co2_range']
            self.co2 += random.randint(-15, 15)
            self.co2 = max(co2_min, min(co2_max, self.co2))
        
        # Humidité varie normalement
        hum_min, hum_max = CLIMATE_CONFIG['humidity_range']
        self.humidity += random.uniform(-1, 1)
        self.humidity = max(hum_min, min(hum_max, self.humidity))
        
        self.last_update = current_time
    
    def update_control_logic(self):
        """Met à jour la logique de contrôle des actionneurs"""
        # Contrôle ventilateur basé sur température
        if self.temperature > CLIMATE_CONFIG['temp_ventilation_on']:
            self.ventilator_on = True
        elif self.temperature < CLIMATE_CONFIG['temp_ventilation_off']:
            self.ventilator_on = False
        
        # Contrôle ventilation forcée basé sur CO₂
        if self.co2 > CLIMATE_CONFIG['co2_forced_ventilation']:
            self.forced_ventilation = True
        elif self.co2 < CLIMATE_CONFIG['co2_normal']:
            self.forced_ventilation = False
    
    def force_scenario(self, scenario_type, duration):
        """Force un scénario spécifique pendant une durée donnée"""
        self.scenario_active = True
        self.scenario_end_time = time.time() + duration
        
        if scenario_type == 'high_temperature':
            self.forced_temp = 32.0
        elif scenario_type == 'low_temperature':
            self.forced_temp = 22.0
        elif scenario_type == 'high_co2':
            self.forced_co2 = 1200
    
    def get_status(self):
        """Retourne l'état actuel du module"""
        return {
            'temperature': round(self.temperature, 1),
            'humidity': round(self.humidity, 1),
            'co2': self.co2,
            'ventilator_on': self.ventilator_on,
            'forced_ventilation': self.forced_ventilation,
            'scenario_active': self.scenario_active,
        }
    
    def get_alarms(self):
        """Retourne les alarmes actives"""
        alarms = []
        
        if self.temperature > CLIMATE_CONFIG['temp_ventilation_on']:
            alarms.append(f"Température élevée: {self.temperature:.1f}°C")
        
        if self.co2 > CLIMATE_CONFIG['co2_forced_ventilation']:
            alarms.append(f"CO₂ élevé: {self.co2} ppm")
        
        return alarms