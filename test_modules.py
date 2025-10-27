"""
Script de test rapide pour vérifier le fonctionnement des modules
Utile pour debug et vérification avant utilisation complète
"""

import time
from climate_module import ClimateModule
from presence_module import PresenceModule
from battery_module import BatteryModule


def test_climate_module():
    """Test du module Climate & Air Quality"""
    print("🌡️ Test du module Climate...")
    
    climate = ClimateModule()
    
    print("État initial:")
    print(f"  - Température: {climate.temperature}°C")
    print(f"  - Humidité: {climate.humidity}%")
    print(f"  - CO₂: {climate.co2} ppm")
    print(f"  - Ventilateur: {'ON' if climate.ventilator_on else 'OFF'}")
    
    # Test scénario température élevée
    print("\\nTest scénario température élevée...")
    climate.force_scenario('high_temperature', 5)
    
    for i in range(3):
        climate.update_sensors()
        climate.update_control_logic()
        status = climate.get_status()
        alarms = climate.get_alarms()
        
        print(f"  Cycle {i+1}: {status['temperature']}°C, Ventilateur: {'ON' if status['ventilator_on'] else 'OFF'}")
        if alarms:
            print(f"    Alarmes: {alarms}")
        time.sleep(1)
    
    print("✅ Module Climate testé\\n")


def test_presence_module():
    """Test du module Presence Detection"""
    print("👥 Test du module Presence...")
    
    presence = PresenceModule()
    
    print("État initial:")
    print(f"  - Mouvement: {'OUI' if presence.movement_detected else 'NON'}")
    print(f"  - Personnes: {presence.persons_count}")
    print(f"  - Lampes: {'ON' if presence.lights_on else 'OFF'}")
    
    # Test scénario présence détectée
    print("\\nTest scénario présence détectée...")
    presence.force_scenario('presence_detected', 5)
    
    for i in range(3):
        presence.update_sensors()
        presence.update_control_logic()
        status = presence.get_status()
        alarms = presence.get_alarms()
        
        print(f"  Cycle {i+1}: {status['persons_count']} personnes, Mouvement: {'OUI' if status['movement_detected'] else 'NON'}, Lampes: {'ON' if status['lights_on'] else 'OFF'}")
        if alarms:
            print(f"    Alarmes: {alarms}")
        time.sleep(1)
    
    print("✅ Module Presence testé\\n")


def test_battery_module():
    """Test du module Battery Monitoring"""
    print("🔋 Test du module Battery...")
    
    battery = BatteryModule()
    
    print("État initial:")
    print(f"  - Tension: {battery.voltage}V")
    print(f"  - Courant: {battery.current}A")
    print(f"  - Température: {battery.temperature}°C")
    print(f"  - Statut: {battery.battery_status}")
    
    # Test scénario batterie faible
    print("\\nTest scénario batterie critique...")
    battery.force_scenario('critical_battery', 5)
    
    for i in range(3):
        battery.update_sensors()
        battery.update_control_logic()
        status = battery.get_status()
        alarms = battery.get_alarms()
        
        print(f"  Cycle {i+1}: {status['voltage']}V, Statut: {status['battery_status']}, PowerSave: {'ON' if status['power_save_mode'] else 'OFF'}")
        if alarms:
            print(f"    Alarmes: {alarms}")
        time.sleep(1)
    
    print("✅ Module Battery testé\\n")


def test_all_modules():
    """Test complet de tous les modules"""
    print("🎯 TEST COMPLET - SIMULATION MONITORING INTELLIGENT")
    print("=" * 60)
    
    # Test individuel des modules
    test_climate_module()
    test_presence_module()
    test_battery_module()
    
    # Test intégré
    print("🔄 Test intégré - simulation 10 secondes...")
    
    climate = ClimateModule()
    presence = PresenceModule()
    battery = BatteryModule()
    
    start_time = time.time()
    
    while time.time() - start_time < 10:
        # Mettre à jour tous les modules
        climate.update_sensors()
        climate.update_control_logic()
        
        presence.update_sensors()
        presence.update_control_logic()
        
        battery.update_sensors()
        battery.update_control_logic()
        
        # Afficher statut toutes les 2 secondes
        if int(time.time() - start_time) % 2 == 0:
            c_status = climate.get_status()
            p_status = presence.get_status()
            b_status = battery.get_status()
            
            print(f"T+{int(time.time() - start_time)}s: Temp={c_status['temperature']}°C, Personnes={p_status['persons_count']}, Batterie={b_status['voltage']}V")
        
        time.sleep(0.5)
    
    print("✅ Test intégré terminé")
    print("\\n🎉 Tous les tests sont réussis ! Vous pouvez lancer main.py")


if __name__ == "__main__":
    test_all_modules()