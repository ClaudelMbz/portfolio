"""
Module de simulation Presence Detection
Gère la détection de mouvement, nombre de personnes et contrôle des lampes
"""

import random
import time
from config import PRESENCE_CONFIG


class PresenceModule:
    def __init__(self):
        self.movement_detected = False
        self.persons_count = 0
        self.lights_on = False
        self.last_movement_time = 0
        self.last_update = time.time()
        
        # Variables pour scénarios forcés
        self.scenario_active = False
        self.scenario_end_time = 0
        self.forced_movement = None
        self.forced_persons = None
    
    def update_sensors(self):
        """Met à jour les valeurs des capteurs simulés"""
        current_time = time.time()
        
        # Vérifier si un scénario forcé est actif
        if self.scenario_active and current_time > self.scenario_end_time:
            self.scenario_active = False
            self.forced_movement = None
            self.forced_persons = None
        
        # Générer valeurs aléatoires ou utiliser valeurs forcées
        if self.forced_movement is not None:
            self.movement_detected = self.forced_movement
            if self.movement_detected:
                self.last_movement_time = current_time
        else:
            # Simulation normale du mouvement
            movement_prob = PRESENCE_CONFIG['movement_probability']
            if self.persons_count > 0:
                movement_prob *= (1 + self.persons_count * 0.2)  # Plus de personnes = plus de mouvement
            
            self.movement_detected = random.random() < movement_prob
            if self.movement_detected:
                self.last_movement_time = current_time
        
        if self.forced_persons is not None:
            self.persons_count = self.forced_persons
        else:
            # Variation normale du nombre de personnes
            if random.random() < 0.1:  # 10% de chance de changement
                change = random.choice([-1, 0, 1])
                self.persons_count = max(0, min(PRESENCE_CONFIG['max_persons'], 
                                               self.persons_count + change))
        
        self.last_update = current_time
    
    def update_control_logic(self):
        """Met à jour la logique de contrôle des actionneurs avec logging détaillé"""
        current_time = time.time()
        previous_lights_state = self.lights_on
        
        # LOGIQUE 1: Allumer les lampes si mouvement détecté
        if self.movement_detected and not self.lights_on:
            self.lights_on = True
            print(f"[PRESENCE] 💡 LAMPES ALLUMÉES: Mouvement détecté ({self.persons_count} pers.)")
        
        # LOGIQUE 2: Allumer/maintenir si des personnes sont présentes
        if self.persons_count > 0 and not self.lights_on:
            self.lights_on = True
            print(f"[PRESENCE] 💡 LAMPES ALLUMÉES: {self.persons_count} personne(s) présente(s)")
        
        # LOGIQUE 3: Éteindre les lampes si aucune présence pendant X secondes
        time_since_movement = current_time - self.last_movement_time if self.last_movement_time > 0 else float('inf')
        
        if (self.persons_count == 0 and 
            self.lights_on and 
            time_since_movement > PRESENCE_CONFIG['light_off_delay']):
            self.lights_on = False
            print(f"[PRESENCE] 💡 LAMPES ÉTEINTES: Aucune présence depuis {time_since_movement:.1f}s")
        
        # LOGIQUE 4: Maintenir allumées si présence continue
        if self.persons_count > 0:
            self.lights_on = True
        
        # Logger les changements d'état
        if previous_lights_state != self.lights_on:
            state = "ALLUMÉES" if self.lights_on else "ÉTEINTES"
            reason = ""
            if self.lights_on:
                if self.movement_detected:
                    reason = f"(mouvement + {self.persons_count} pers.)"
                elif self.persons_count > 0:
                    reason = f"({self.persons_count} personne(s) présente(s))"
            else:
                reason = f"(absence depuis {time_since_movement:.1f}s)"
            
            print(f"[CONTROL] 💡 ÉCLAIRAGE {state} {reason}")
    
    def force_scenario(self, scenario_type, duration):
        """Force un scénario spécifique pendant une durée donnée"""
        self.scenario_active = True
        self.scenario_end_time = time.time() + duration
        
        if scenario_type == 'presence_detected':
            self.forced_movement = True
            self.forced_persons = 3
        elif scenario_type == 'no_presence':
            self.forced_movement = False
            self.forced_persons = 0
    
    def get_status(self):
        """Retourne l'état actuel du module"""
        current_time = time.time()
        time_since_movement = current_time - self.last_movement_time if self.last_movement_time > 0 else float('inf')
        
        return {
            'movement_detected': self.movement_detected,
            'persons_count': self.persons_count,
            'lights_on': self.lights_on,
            'time_since_movement': round(time_since_movement, 1) if time_since_movement != float('inf') else None,
            'scenario_active': self.scenario_active,
        }
    
    def get_alarms(self):
        """Retourne les alarmes actives"""
        alarms = []
        
        current_time = time.time()
        if (self.persons_count == 0 and self.lights_on and 
            current_time - self.last_movement_time > PRESENCE_CONFIG['light_off_delay'] * 2):
            alarms.append("Lampes allumées sans présence détectée")
        
        return alarms