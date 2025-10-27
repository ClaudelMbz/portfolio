"""
Module de simulation Battery Monitoring
Gère la tension, courant, température batterie avec alertes et modes d'économie
"""

import random
import time
from config import BATTERY_CONFIG


class BatteryModule:
    def __init__(self):
        self.voltage = 12.5
        self.current = 2.0
        self.temperature = 25.0
        self.battery_status = 'Normal'  # Normal, Low, Critical, Shutdown
        self.power_save_mode = False
        self.last_update = time.time()
        
        # Variables pour scénarios forcés
        self.scenario_active = False
        self.scenario_end_time = 0
        self.forced_voltage = None
        self.forced_current = None
    
    def update_sensors(self):
        """Met à jour les valeurs des capteurs simulés"""
        current_time = time.time()
        
        # Vérifier si un scénario forcé est actif
        if self.scenario_active and current_time > self.scenario_end_time:
            self.scenario_active = False
            self.forced_voltage = None
            self.forced_current = None
        
        # Générer valeurs aléatoires ou utiliser valeurs forcées
        if self.forced_voltage is not None:
            self.voltage = self.forced_voltage + random.uniform(-0.1, 0.1)
        else:
            # Variation normale de tension
            volt_min, volt_max = BATTERY_CONFIG['voltage_range']
            
            # Tendance de décharge lente normale
            discharge_rate = random.uniform(-0.01, 0.02)  # Légère décharge
            self.voltage += discharge_rate
            
            # Fluctuation aléatoire
            self.voltage += random.uniform(-0.05, 0.05)
            self.voltage = max(volt_min, min(volt_max, self.voltage))
        
        if self.forced_current is not None:
            self.current = self.forced_current + random.uniform(-0.2, 0.2)
        else:
            # Variation normale du courant
            curr_min, curr_max = BATTERY_CONFIG['current_range']
            self.current += random.uniform(-0.3, 0.3)
            self.current = max(curr_min, min(curr_max, self.current))
        
        # Température batterie varie avec l'utilisation
        temp_min, temp_max = BATTERY_CONFIG['temp_range']
        # Plus de courant = plus de chaleur
        temp_influence = (self.current / 5.0) * 2.0  # Influence du courant sur la température
        self.temperature += random.uniform(-0.5, 0.5) + temp_influence * 0.1
        self.temperature = max(temp_min, min(temp_max, self.temperature))
        
        self.last_update = current_time
    
    def update_control_logic(self):
        """Met à jour la logique de contrôle et les alertes"""
        # Déterminer le statut de la batterie
        if self.voltage < BATTERY_CONFIG['voltage_shutdown']:
            self.battery_status = 'Shutdown'
            self.power_save_mode = True
        elif self.voltage < BATTERY_CONFIG['voltage_critical']:
            self.battery_status = 'Critical'
            self.power_save_mode = True
        elif self.voltage < BATTERY_CONFIG['voltage_low']:
            self.battery_status = 'Low'
            self.power_save_mode = False
        else:
            self.battery_status = 'Normal'
            self.power_save_mode = False
    
    def force_scenario(self, scenario_type, duration):
        """Force un scénario spécifique pendant une durée donnée"""
        self.scenario_active = True
        self.scenario_end_time = time.time() + duration
        
        if scenario_type == 'low_battery':
            self.forced_voltage = 10.5
            self.forced_current = 1.0
        elif scenario_type == 'critical_battery':
            self.forced_voltage = 9.8
            self.forced_current = 0.5
    
    def get_status(self):
        """Retourne l'état actuel du module"""
        # Calculer la capacité estimée (approximative)
        voltage_range = BATTERY_CONFIG['voltage_range'][1] - BATTERY_CONFIG['voltage_range'][0]
        capacity_percent = ((self.voltage - BATTERY_CONFIG['voltage_range'][0]) / voltage_range) * 100
        capacity_percent = max(0, min(100, capacity_percent))
        
        return {
            'voltage': round(self.voltage, 2),
            'current': round(self.current, 2),
            'temperature': round(self.temperature, 1),
            'battery_status': self.battery_status,
            'power_save_mode': self.power_save_mode,
            'capacity_percent': round(capacity_percent, 1),
            'scenario_active': self.scenario_active,
        }
    
    def get_alarms(self):
        """Retourne les alarmes actives"""
        alarms = []
        
        if self.battery_status == 'Shutdown':
            alarms.append(f"CRITIQUE: Arrêt système imminent - {self.voltage:.2f}V")
        elif self.battery_status == 'Critical':
            alarms.append(f"Batterie critique - {self.voltage:.2f}V")
        elif self.battery_status == 'Low':
            alarms.append(f"Batterie faible - {self.voltage:.2f}V")
        
        if self.temperature > 45:
            alarms.append(f"Température batterie élevée: {self.temperature:.1f}°C")
        
        if self.current > 8:
            alarms.append(f"Courant élevé: {self.current:.1f}A")
        
        return alarms