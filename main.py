"""
Simulation de Monitoring Intelligent
Système de simulation avec modules Climate, Presence, Battery et interface HMI

Exécution : python main.py
"""

import tkinter as tk
import threading
import time
import signal
import sys
from config import UPDATE_INTERVAL

# Import des modules
from climate_module import ClimateModule
from presence_module import PresenceModule
from battery_module import BatteryModule
from hmi_interface import HMIInterface
from scenario_manager import ScenarioManager


class MonitoringSimulation:
    def __init__(self):
        self.running = False
        
        # Initialiser les modules
        print("🚀 Démarrage de la simulation de monitoring intelligent...")
        
        self.climate_module = ClimateModule()
        self.presence_module = PresenceModule()
        self.battery_module = BatteryModule()
        
        print("✅ Modules initialisés : Climate, Presence, Battery")
        
        # Interface graphique
        self.root = tk.Tk()
        self.hmi_interface = HMIInterface(
            self.root, 
            self.climate_module, 
            self.presence_module, 
            self.battery_module
        )
        
        print("✅ Interface HMI créée")
        
        # Gestionnaire de scénarios
        self.scenario_manager = ScenarioManager(
            self.climate_module,
            self.presence_module,
            self.battery_module,
            self.hmi_interface
        )
        
        print("✅ Gestionnaire de scénarios configuré")
        
        # Thread pour la boucle de simulation
        self.simulation_thread = None
        
        # Gestion de l'arrêt propre
        self.setup_signal_handlers()
    
    def setup_signal_handlers(self):
        """Configure les gestionnaires de signaux pour un arrêt propre"""
        def signal_handler(sig, frame):
            print("\\n🛑 Arrêt demandé...")
            self.stop()
            sys.exit(0)
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
    
    def start(self):
        """Démarre la simulation complète"""
        self.running = True
        
        # Démarrer la boucle de simulation dans un thread séparé
        self.simulation_thread = threading.Thread(target=self._simulation_loop, daemon=True)
        self.simulation_thread.start()
        
        # Démarrer le gestionnaire de scénarios
        self.scenario_manager.start()
        
        print("✅ Simulation démarrée")
        print(f"📊 Interface graphique en cours d'exécution...")
        print(f"⏱️  Intervalle de mise à jour : {UPDATE_INTERVAL}s")
        print("🎮 Utilisez les boutons dans l'interface pour déclencher des scénarios manuels")
        print("🤖 Les scénarios automatiques se déclenchent toutes les ~10s")
        print("\\n" + "="*60)
        
        # Démarrer l'interface graphique (bloquant)
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            self.stop()
    
    def stop(self):
        """Arrête la simulation"""
        if self.running:
            print("\\n🛑 Arrêt de la simulation en cours...")
            
            self.running = False
            
            # Arrêter le gestionnaire de scénarios
            self.scenario_manager.stop()
            
            # Fermer l'interface graphique si elle existe
            if self.root:
                try:
                    self.root.quit()
                    self.root.destroy()
                except:
                    pass
            
            print("✅ Simulation arrêtée proprement")
    
    def _simulation_loop(self):
        """Boucle principale de simulation"""
        print("🔄 Boucle de simulation démarrée")
        
        while self.running:
            try:
                # Mettre à jour tous les capteurs
                self.climate_module.update_sensors()
                self.presence_module.update_sensors()
                self.battery_module.update_sensors()
                
                # Appliquer la logique de contrôle
                self.climate_module.update_control_logic()
                self.presence_module.update_control_logic()
                self.battery_module.update_control_logic()
                
                # Attendre avant la prochaine itération
                time.sleep(UPDATE_INTERVAL)
                
            except Exception as e:
                print(f"❌ Erreur dans la boucle de simulation: {e}")
                time.sleep(1)
        
        print("🛑 Boucle de simulation arrêtée")
    
    def print_system_status(self):
        """Affiche le statut du système (pour debug)"""
        print("\\n" + "="*50)
        print("📊 STATUT SYSTÈME")
        print("="*50)
        
        # Statut Climate
        climate_status = self.climate_module.get_status()
        print(f"🌡️  Climate: {climate_status['temperature']}°C, {climate_status['humidity']}%, CO₂:{climate_status['co2']}ppm")
        print(f"   Ventilateur: {'ON' if climate_status['ventilator_on'] else 'OFF'}")
        
        # Statut Presence  
        presence_status = self.presence_module.get_status()
        print(f"👥 Presence: {presence_status['persons_count']} personnes, Mouvement: {'OUI' if presence_status['movement_detected'] else 'NON'}")
        print(f"   Lampes: {'ON' if presence_status['lights_on'] else 'OFF'}")
        
        # Statut Battery
        battery_status = self.battery_module.get_status()
        print(f"🔋 Battery: {battery_status['voltage']}V, {battery_status['current']}A, {battery_status['temperature']}°C")
        print(f"   Statut: {battery_status['battery_status']}, PowerSave: {'ON' if battery_status['power_save_mode'] else 'OFF'}")
        
        # Statut gestionnaire de scénarios
        scenario_status = self.scenario_manager.get_status()
        print(f"🤖 Scénarios: {scenario_status['total_scenarios']} total, prochain dans {scenario_status['time_to_next_scenario']}s")
        
        print("="*50)


def main():
    """Fonction principale"""
    print("🎯 SIMULATION MONITORING INTELLIGENT")
    print("=" * 40)
    
    # Créer et démarrer la simulation
    simulation = MonitoringSimulation()
    
    try:
        simulation.start()
    except KeyboardInterrupt:
        print("\\n⏹️  Interruption clavier détectée")
    except Exception as e:
        print(f"❌ Erreur fatale: {e}")
    finally:
        simulation.stop()


if __name__ == "__main__":
    main()