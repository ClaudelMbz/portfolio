"""
Gestionnaire de scénarios automatiques
Déclenche des scénarios prédéfinis après un délai configurable
"""

import threading
import time
import random
from config import SCENARIO_DELAY, SCENARIOS


class ScenarioManager:
    def __init__(self, climate_module, presence_module, battery_module, hmi_interface=None):
        self.climate_module = climate_module
        self.presence_module = presence_module
        self.battery_module = battery_module
        self.hmi_interface = hmi_interface
        
        self.running = False
        self.thread = None
        self.start_time = time.time()
        self.next_scenario_time = time.time() + SCENARIO_DELAY
        self.scenario_history = []
    
    def start(self):
        """Démarre le gestionnaire de scénarios automatiques"""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run_scenarios, daemon=True)
            self.thread.start()
            print(f"Gestionnaire de scénarios démarré. Premier scénario dans {SCENARIO_DELAY}s")
    
    def stop(self):
        """Arrête le gestionnaire de scénarios"""
        self.running = False
        if self.thread:
            self.thread.join()
        print("Gestionnaire de scénarios arrêté")
    
    def _run_scenarios(self):
        """Boucle principale du gestionnaire de scénarios"""
        while self.running:
            current_time = time.time()
            
            # Vérifier s'il est temps de déclencher un scénario
            if current_time >= self.next_scenario_time:
                self._trigger_random_scenario()
                
                # Programmer le prochain scénario
                next_delay = random.uniform(SCENARIO_DELAY * 0.8, SCENARIO_DELAY * 1.2)
                self.next_scenario_time = current_time + next_delay
                
                print(f"Prochain scénario automatique dans {next_delay:.1f}s")
            
            # Dormir un peu pour éviter une consommation CPU excessive
            time.sleep(1)
    
    def _trigger_random_scenario(self):
        """Déclenche un scénario aléatoire"""
        # Obtenir la liste des scénarios disponibles
        available_scenarios = list(SCENARIOS.keys())
        
        # Éviter de répéter le même scénario consécutivement
        if self.scenario_history:
            last_scenario = self.scenario_history[-1]['name']
            if last_scenario in available_scenarios and len(available_scenarios) > 1:
                available_scenarios.remove(last_scenario)
        
        # Sélectionner un scénario aléatoire
        scenario_name = random.choice(available_scenarios)
        scenario_config = SCENARIOS[scenario_name]
        duration = scenario_config['duration']
        
        # Déclencher le scénario dans le bon module
        module_name = self._get_module_for_scenario(scenario_name)
        
        if module_name == 'climate':
            self.climate_module.force_scenario(scenario_name, duration)
        elif module_name == 'presence':
            self.presence_module.force_scenario(scenario_name, duration)
        elif module_name == 'battery':
            self.battery_module.force_scenario(scenario_name, duration)
        
        # Enregistrer dans l'historique
        scenario_record = {
            'name': scenario_name,
            'module': module_name,
            'duration': duration,
            'timestamp': time.time(),
            'trigger_type': 'automatic'
        }
        self.scenario_history.append(scenario_record)
        
        # Limiter l'historique à 50 entrées
        if len(self.scenario_history) > 50:
            self.scenario_history.pop(0)
        
        # Messages détaillés pour l'interface
        scenario_descriptions = {
            'high_temperature': {
                'start': f'🔥 SCÉNARIO AUTO: Température critique (32°C) pendant {duration}s',
                'action': 'Test automatique du système de ventilation et alertes thermiques'
            },
            'low_temperature': {
                'start': f'❄️ SCÉNARIO AUTO: Température basse (22°C) pendant {duration}s',
                'action': 'Test du système de chauffage et gestion thermique'
            },
            'high_co2': {
                'start': f'💨 SCÉNARIO AUTO: CO₂ dangereux (1200ppm) pendant {duration}s',
                'action': 'Test ventilation forcée et purification air'
            },
            'low_battery': {
                'start': f'🔋 SCÉNARIO AUTO: Batterie faible (10.5V) pendant {duration}s',
                'action': 'Test alertes énergétiques et gestion consommation'
            },
            'critical_battery': {
                'start': f'⚡ SCÉNARIO AUTO: Batterie critique (9.8V) pendant {duration}s',
                'action': 'Test mode économie d\'urgence et procédures sécurité'
            },
            'presence_detected': {
                'start': f'👥 SCÉNARIO AUTO: Présence détectée (3 pers.) pendant {duration}s',
                'action': 'Test éclairage automatique et gestion occupation'
            },
            'no_presence': {
                'start': f'🚫 SCÉNARIO AUTO: Absence totale pendant {duration}s',
                'action': 'Test extinction automatique et mode veille'
            }
        }
        
        scenario_info = scenario_descriptions.get(scenario_name, {
            'start': f'Scénario {scenario_name}',
            'action': 'Test automatique du système'
        })
        
        print(f"[SCENARIO] {scenario_info['start']}")
        print(f"[ACTION] {scenario_info['action']}")
        
        if self.hmi_interface:
            # Logger le déclenchement du scénario
            self.hmi_interface.log_event(scenario_info['start'], "SCENARIO")
            
            # Logger l'action attendue
            self.hmi_interface.log_event(f"⚙️ ACTION: {scenario_info['action']}", "ACTION")
            
            # Logger les détails techniques
            end_time = time.strftime("%H:%M:%S", time.localtime(time.time() + duration))
            self.hmi_interface.log_event(f"⏰ Durée: {duration}s - Fin prévue: {end_time}", "INFO")
            
            # Séparateur visuel
            self.hmi_interface.log_event("-" * 40, "INFO", False)
    
    def _get_module_for_scenario(self, scenario_name):
        """Retourne le nom du module responsable d'un scénario"""
        climate_scenarios = ['high_temperature', 'low_temperature', 'high_co2']
        presence_scenarios = ['presence_detected', 'no_presence']
        battery_scenarios = ['low_battery', 'critical_battery']
        
        if scenario_name in climate_scenarios:
            return 'climate'
        elif scenario_name in presence_scenarios:
            return 'presence'
        elif scenario_name in battery_scenarios:
            return 'battery'
        else:
            return 'unknown'
    
    def trigger_manual_scenario(self, scenario_name):
        """Déclenche manuellement un scénario spécifique"""
        if scenario_name in SCENARIOS:
            scenario_config = SCENARIOS[scenario_name]
            duration = scenario_config['duration']
            
            # Déclencher le scénario
            module_name = self._get_module_for_scenario(scenario_name)
            
            if module_name == 'climate':
                self.climate_module.force_scenario(scenario_name, duration)
            elif module_name == 'presence':
                self.presence_module.force_scenario(scenario_name, duration)
            elif module_name == 'battery':
                self.battery_module.force_scenario(scenario_name, duration)
            
            # Enregistrer dans l'historique
            scenario_record = {
                'name': scenario_name,
                'module': module_name,
                'duration': duration,
                'timestamp': time.time(),
                'trigger_type': 'manual'
            }
            self.scenario_history.append(scenario_record)
            
            print(f"[SCENARIO] Scénario manuel '{scenario_name}' déclenché pour {duration}s")
            return True
        
        return False
    
    def get_status(self):
        """Retourne l'état actuel du gestionnaire"""
        current_time = time.time()
        time_to_next = max(0, self.next_scenario_time - current_time)
        
        return {
            'running': self.running,
            'time_to_next_scenario': round(time_to_next, 1),
            'total_scenarios': len(self.scenario_history),
            'uptime': round(current_time - self.start_time, 1),
        }
    
    def get_scenario_history(self, limit=10):
        """Retourne l'historique des scénarios récents"""
        return self.scenario_history[-limit:] if limit else self.scenario_history