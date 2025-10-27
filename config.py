"""
Configuration du système de simulation de monitoring intelligent
"""

# Intervalle de mise à jour principal (en secondes)
UPDATE_INTERVAL = 2.0

# Délai avant déclenchement des scénarios automatiques (en secondes)
SCENARIO_DELAY = 10.0

# Configuration Climate & Air Quality
CLIMATE_CONFIG = {
    'temp_range': (20, 35),          # Plage température (°C)
    'humidity_range': (30, 80),      # Plage humidité (%)
    'co2_range': (400, 1500),        # Plage CO₂ (ppm)
    'temp_ventilation_on': 28,       # Seuil activation ventilateur (°C)
    'temp_ventilation_off': 26,      # Seuil désactivation ventilateur (°C)
    'co2_forced_ventilation': 1000,  # Seuil ventilation forcée (ppm)
    'co2_normal': 800,               # Retour normal (ppm)
}

# Configuration Presence Detection
PRESENCE_CONFIG = {
    'max_persons': 5,                # Nombre max de personnes
    'light_off_delay': 5,            # Délai extinction lampes (secondes)
    'movement_probability': 0.3,     # Probabilité de mouvement par cycle
}

# Configuration Battery Monitoring
BATTERY_CONFIG = {
    'voltage_range': (9.0, 13.0),   # Plage tension (V)
    'current_range': (0, 10),       # Plage courant (A)
    'temp_range': (20, 50),         # Plage température batterie (°C)
    'voltage_low': 11.0,            # Seuil batterie faible (V)
    'voltage_critical': 10.0,       # Seuil batterie critique (V)
    'voltage_shutdown': 9.5,        # Seuil arrêt système (V)
}

# Configuration HMI
HMI_CONFIG = {
    'window_title': 'Simulation Monitoring Intelligent',
    'window_size': '1000x700',
    'refresh_rate': 1000,           # Rafraîchissement interface (ms)
}

# Scénarios de simulation automatique
SCENARIOS = {
    'high_temperature': {'temp': 32, 'duration': 30},
    'low_temperature': {'temp': 22, 'duration': 20},
    'high_co2': {'co2': 1200, 'duration': 25},
    'low_battery': {'voltage': 10.5, 'duration': 40},
    'critical_battery': {'voltage': 9.8, 'duration': 15},
    'presence_detected': {'persons': 3, 'movement': True, 'duration': 20},
    'no_presence': {'persons': 0, 'movement': False, 'duration': 15},
}