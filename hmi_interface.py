"""
Interface utilisateur (HMI) pour la simulation de monitoring intelligent
Design moderne avec thème sombre et animations
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
import time
from config import HMI_CONFIG, SCENARIOS


class HMIInterface:
    def __init__(self, root, climate_module, presence_module, battery_module):
        self.root = root
        self.climate_module = climate_module
        self.presence_module = presence_module
        self.battery_module = battery_module
        
        # Couleurs du thème moderne
        self.colors = {
            'bg_primary': '#1e1e1e',     # Fond principal sombre
            'bg_secondary': '#2d2d2d',   # Fond cartes
            'bg_accent': '#3e3e3e',      # Accents
            'text_primary': '#ffffff',   # Texte principal
            'text_secondary': '#b0b0b0', # Texte secondaire
            'accent_blue': '#007acc',    # Bleu moderne
            'accent_green': '#4caf50',   # Vert succès
            'accent_orange': '#ff9800',  # Orange warning
            'accent_red': '#f44336',     # Rouge erreur
            'accent_purple': '#9c27b0',  # Violet
            'border': '#404040',         # Bordures
        }
        
        # Configuration de la fenêtre avec style Windows moderne
        self.root.title('🎯 Monitoring Intelligent - Simulation Avancée')
        self.root.geometry('1400x900')
        self.root.configure(bg=self.colors['bg_primary'])
        self.root.resizable(True, True)
        self.root.minsize(1200, 700)
        
        # Centrer la fenêtre
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (1400 // 2)
        y = (self.root.winfo_screenheight() // 2) - (900 // 2)
        self.root.geometry(f'1400x900+{x}+{y}')
        
        # Variables pour les labels dynamiques
        self.status_vars = {}
        self.setup_styles()
        self.create_interface()
        
        # Démarrer la mise à jour automatique
        self.update_display()
    
    def setup_styles(self):
        """Configure les styles pour l'interface moderne"""
        style = ttk.Style()
        
        # Style pour les frames principales
        style.configure('Card.TFrame', 
                       background=self.colors['bg_secondary'],
                       relief='flat', borderwidth=1)
        
        # Style pour les labels de titre
        style.configure('CardTitle.TLabel',
                       background=self.colors['bg_secondary'],
                       foreground=self.colors['text_primary'],
                       font=('Segoe UI', 14, 'bold'))
        
        # Style pour les labels de valeur
        style.configure('Value.TLabel',
                       background=self.colors['bg_secondary'],
                       foreground=self.colors['accent_blue'],
                       font=('Consolas', 12, 'bold'))
        
        # Style pour les boutons
        style.configure('Modern.TButton',
                       background=self.colors['accent_blue'],
                       foreground='white',
                       focuscolor='none',
                       borderwidth=0,
                       font=('Segoe UI', 9))
        
        style.map('Modern.TButton',
                 background=[('active', '#005999'),
                            ('pressed', '#004080')])
    
    def create_interface(self):
        """Crée l'interface graphique moderne"""
        # Header avec titre et statut
        self.create_header()
        
        # Conteneur principal avec grille
        main_container = tk.Frame(self.root, bg=self.colors['bg_primary'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Grille 3x2 pour inclure le journal en haut à droite
        main_container.grid_columnconfigure(0, weight=2)  # Modules principaux plus larges
        main_container.grid_columnconfigure(1, weight=1)  # Colonne droite pour journal
        main_container.grid_rowconfigure(0, weight=1)     # Ligne du haut
        main_container.grid_rowconfigure(1, weight=1)     # Ligne du milieu
        main_container.grid_rowconfigure(2, weight=1)     # Ligne du bas
        
        # Modules dans la colonne gauche
        self.create_climate_card(main_container, 0, 0)
        self.create_presence_card(main_container, 1, 0)
        self.create_battery_card(main_container, 2, 0)
        
        # Journal des événements en haut à droite (occupe 2 lignes)
        self.create_events_journal(main_container, 0, 1, 2)
        
        # Panel de contrôle en bas à droite
        self.create_control_panel(main_container, 2, 1)
    
    def create_header(self):
        """Crée l'en-tête moderne"""
        header = tk.Frame(self.root, bg=self.colors['bg_secondary'], height=80)
        header.pack(fill=tk.X, padx=0, pady=0)
        header.pack_propagate(False)
        
        # Titre principal avec style moderne
        title_frame = tk.Frame(header, bg=self.colors['bg_secondary'])
        title_frame.pack(expand=True, fill=tk.BOTH)
        
        title = tk.Label(title_frame, 
                        text="🎯 MONITORING INTELLIGENT",
                        font=('Segoe UI', 24, 'bold'),
                        bg=self.colors['bg_secondary'],
                        fg=self.colors['text_primary'])
        title.pack(side=tk.LEFT, padx=20, pady=20)
        
        # Indicateur de statut système avec horloge temps réel
        status_frame = tk.Frame(title_frame, bg=self.colors['bg_secondary'])
        status_frame.pack(side=tk.RIGHT, padx=20, pady=20)
        
        self.system_clock = tk.Label(status_frame,
                                    text=time.strftime("%H:%M:%S"),
                                    font=('Consolas', 11, 'bold'),
                                    bg=self.colors['bg_secondary'],
                                    fg=self.colors['text_secondary'])
        self.system_clock.pack()
        
        self.system_status = tk.Label(status_frame,
                                     text="🟢 SYSTÈME ACTIF",
                                     font=('Segoe UI', 12, 'bold'),
                                     bg=self.colors['bg_secondary'],
                                     fg=self.colors['accent_green'])
        self.system_status.pack()
    
    def create_climate_card(self, parent, row, col):
        """Crée la carte Climate & Air Quality moderne"""
        # Container avec effet d'ombre simulé
        shadow_frame = tk.Frame(parent, bg='#0a0a0a', relief='flat')
        shadow_frame.grid(row=row, column=col, padx=12, pady=12, sticky='nsew')
        
        card = tk.Frame(shadow_frame, bg=self.colors['bg_secondary'], relief='flat')
        card.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # En-tête de la carte
        header = tk.Frame(card, bg=self.colors['accent_blue'], height=50)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        title = tk.Label(header, text="🌡️ CLIMATE CONTROL",
                        font=('Segoe UI', 14, 'bold'),
                        bg=self.colors['accent_blue'],
                        fg='white')
        title.pack(pady=12)
        
        # Corps de la carte
        body = tk.Frame(card, bg=self.colors['bg_secondary'])
        body.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Métriques principales
        metrics = tk.Frame(body, bg=self.colors['bg_secondary'])
        metrics.pack(fill=tk.X, pady=(0, 15))
        
        # Température avec indicateur visuel
        temp_frame = self.create_metric_widget(metrics, "TEMPÉRATURE", "temp_display", "°C", self.colors['accent_red'])
        temp_frame.pack(fill=tk.X, pady=5)
        
        # Humidité
        humid_frame = self.create_metric_widget(metrics, "HUMIDITÉ", "humidity_display", "%", self.colors['accent_blue'])
        humid_frame.pack(fill=tk.X, pady=5)
        
        # CO₂
        co2_frame = self.create_metric_widget(metrics, "CO₂", "co2_display", "ppm", self.colors['accent_orange'])
        co2_frame.pack(fill=tk.X, pady=5)
        
        # Ligne de séparation
        separator = tk.Frame(body, bg=self.colors['border'], height=1)
        separator.pack(fill=tk.X, pady=10)
        
        # État des actionneurs avec indicateurs LED
        actuators = tk.Frame(body, bg=self.colors['bg_secondary'])
        actuators.pack(fill=tk.X)
        
        self.status_vars['ventilator_led'] = tk.StringVar(value="🔴")
        self.status_vars['forced_vent_led'] = tk.StringVar(value="🔴")
        
        self.create_actuator_status(actuators, "Ventilateur", "ventilator_led", "ventilator_status")
        self.create_actuator_status(actuators, "Ventilation forcée", "forced_vent_led", "forced_vent_status")
    
    def create_presence_card(self, parent, row, col):
        """Crée la carte Presence Detection moderne"""
        # Container avec effet d'ombre simulé
        shadow_frame = tk.Frame(parent, bg='#0a0a0a', relief='flat')
        shadow_frame.grid(row=row, column=col, padx=12, pady=12, sticky='nsew')
        
        card = tk.Frame(shadow_frame, bg=self.colors['bg_secondary'], relief='flat')
        card.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # Appliquer coins arrondis
        self.create_rounded_corners(card)
        
        # En-tête de la carte
        header = tk.Frame(card, bg=self.colors['accent_purple'], height=50)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        title = tk.Label(header, text="👥 PRESENCE DETECTION",
                        font=('Segoe UI', 14, 'bold'),
                        bg=self.colors['accent_purple'],
                        fg='white')
        title.pack(pady=12)
        
        # Corps de la carte
        body = tk.Frame(card, bg=self.colors['bg_secondary'])
        body.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Zone de détection visuelle
        detection_zone = tk.Frame(body, bg=self.colors['bg_accent'], height=80)
        detection_zone.pack(fill=tk.X, pady=(0, 15))
        detection_zone.pack_propagate(False)
        
        self.status_vars['movement_indicator'] = tk.StringVar(value="❌")
        self.status_vars['persons_count'] = tk.StringVar(value="0")
        
        # Indicateur de mouvement central
        movement_frame = tk.Frame(detection_zone, bg=self.colors['bg_accent'])
        movement_frame.pack(expand=True)
        
        tk.Label(movement_frame, text="MOUVEMENT DÉTECTÉ",
                font=('Segoe UI', 10, 'bold'),
                bg=self.colors['bg_accent'],
                fg=self.colors['text_secondary']).pack()
        
        movement_status = tk.Label(movement_frame,
                                  textvariable=self.status_vars['movement_indicator'],
                                  font=('Segoe UI', 24),
                                  bg=self.colors['bg_accent'])
        movement_status.pack()
        
        # Métriques
        metrics = tk.Frame(body, bg=self.colors['bg_secondary'])
        metrics.pack(fill=tk.X, pady=10)
        
        persons_frame = self.create_metric_widget(metrics, "PERSONNES", "persons_display", "pers.", self.colors['accent_green'])
        persons_frame.pack(fill=tk.X, pady=5)
        
        time_frame = self.create_metric_widget(metrics, "DERNIER MOUVEMENT", "time_since_display", "sec", self.colors['text_secondary'])
        time_frame.pack(fill=tk.X, pady=5)
        
        # Séparateur
        separator = tk.Frame(body, bg=self.colors['border'], height=1)
        separator.pack(fill=tk.X, pady=10)
        
        # État éclairage
        lighting = tk.Frame(body, bg=self.colors['bg_secondary'])
        lighting.pack(fill=tk.X)
        
        self.status_vars['lights_led'] = tk.StringVar(value="🔴")
        self.create_actuator_status(lighting, "Éclairage", "lights_led", "lights_status")
    
    def create_battery_card(self, parent, row, col):
        """Crée la carte Battery Monitoring moderne"""
        # Container avec effet d'ombre simulé
        shadow_frame = tk.Frame(parent, bg='#0a0a0a', relief='flat')
        shadow_frame.grid(row=row, column=col, padx=12, pady=12, sticky='nsew')
        
        card = tk.Frame(shadow_frame, bg=self.colors['bg_secondary'], relief='flat')
        card.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # Appliquer coins arrondis
        self.create_rounded_corners(card)
        
        # En-tête de la carte
        header = tk.Frame(card, bg=self.colors['accent_green'], height=50)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        title = tk.Label(header, text="🔋 BATTERY MONITORING",
                        font=('Segoe UI', 14, 'bold'),
                        bg=self.colors['accent_green'],
                        fg='white')
        title.pack(pady=12)
        
        # Corps de la carte
        body = tk.Frame(card, bg=self.colors['bg_secondary'])
        body.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Indicateur de capacité visuel
        capacity_frame = tk.Frame(body, bg=self.colors['bg_accent'])
        capacity_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.status_vars['capacity_bar'] = tk.StringVar(value="87.5%")
        self.status_vars['battery_icon'] = tk.StringVar(value="🔋")
        
        # Barre de capacité simulée avec texte
        capacity_display = tk.Frame(capacity_frame, bg=self.colors['bg_accent'])
        capacity_display.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(capacity_display, text="CAPACITÉ",
                font=('Segoe UI', 10, 'bold'),
                bg=self.colors['bg_accent'],
                fg=self.colors['text_secondary']).pack()
        
        battery_display = tk.Frame(capacity_display, bg=self.colors['bg_accent'])
        battery_display.pack()
        
        tk.Label(battery_display,
                textvariable=self.status_vars['battery_icon'],
                font=('Segoe UI', 20),
                bg=self.colors['bg_accent']).pack(side=tk.LEFT)
        
        tk.Label(battery_display,
                textvariable=self.status_vars['capacity_bar'],
                font=('Consolas', 16, 'bold'),
                bg=self.colors['bg_accent'],
                fg=self.colors['accent_green']).pack(side=tk.LEFT, padx=10)
        
        # Métriques détaillées
        metrics = tk.Frame(body, bg=self.colors['bg_secondary'])
        metrics.pack(fill=tk.X, pady=10)
        
        voltage_frame = self.create_metric_widget(metrics, "TENSION", "voltage_display", "V", self.colors['accent_blue'])
        voltage_frame.pack(fill=tk.X, pady=2)
        
        current_frame = self.create_metric_widget(metrics, "COURANT", "current_display", "A", self.colors['accent_orange'])
        current_frame.pack(fill=tk.X, pady=2)
        
        temp_frame = self.create_metric_widget(metrics, "TEMPÉRATURE", "battery_temp_display", "°C", self.colors['accent_red'])
        temp_frame.pack(fill=tk.X, pady=2)
        
        # Séparateur
        separator = tk.Frame(body, bg=self.colors['border'], height=1)
        separator.pack(fill=tk.X, pady=10)
        
        # États système
        status_frame = tk.Frame(body, bg=self.colors['bg_secondary'])
        status_frame.pack(fill=tk.X)
        
        self.status_vars['battery_status_led'] = tk.StringVar(value="🟢")
        self.status_vars['power_save_led'] = tk.StringVar(value="🔴")
        
        self.create_actuator_status(status_frame, "Statut système", "battery_status_led", "battery_status_text")
        self.create_actuator_status(status_frame, "Mode économie", "power_save_led", "power_save_text")
    
    def create_control_panel(self, parent, row, col):
        """Crée le panel de contrôle moderne"""
        # Container avec effet d'ombre simulé
        shadow_frame = tk.Frame(parent, bg='#0a0a0a', relief='flat')
        shadow_frame.grid(row=row, column=col, padx=12, pady=12, sticky='nsew')
        
        card = tk.Frame(shadow_frame, bg=self.colors['bg_secondary'], relief='flat')
        card.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # Appliquer coins arrondis
        self.create_rounded_corners(card)
        
        # En-tête de la carte
        header = tk.Frame(card, bg=self.colors['accent_orange'], height=50)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        title = tk.Label(header, text="🎮 CONTRÔLES SYSTÈME",
                        font=('Segoe UI', 14, 'bold'),
                        bg=self.colors['accent_orange'],
                        fg='white')
        title.pack(pady=12)
        
        # Corps de la carte
        body = tk.Frame(card, bg=self.colors['bg_secondary'])
        body.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Section scénarios
        scenarios_label = tk.Label(body, text="SCÉNARIOS DE TEST",
                                  font=('Segoe UI', 11, 'bold'),
                                  bg=self.colors['bg_secondary'],
                                  fg=self.colors['text_primary'])
        scenarios_label.pack(anchor='w', pady=(0, 10))
        
        # Boutons de scénarios organisés par catégorie
        climate_frame = tk.Frame(body, bg=self.colors['bg_secondary'])
        climate_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(climate_frame, text="🌡️ Climate:",
                font=('Segoe UI', 9, 'bold'),
                bg=self.colors['bg_secondary'],
                fg=self.colors['accent_blue']).pack(anchor='w')
        
        climate_btns = tk.Frame(climate_frame, bg=self.colors['bg_secondary'])
        climate_btns.pack(fill=tk.X, padx=10, pady=2)
        
        self.create_scenario_button(climate_btns, "🔥 Temp Haute", "high_temperature", self.colors['accent_red'])
        self.create_scenario_button(climate_btns, "❄️ Temp Basse", "low_temperature", self.colors['accent_blue'])
        self.create_scenario_button(climate_btns, "💨 CO₂ Élevé", "high_co2", self.colors['accent_orange'])
        
        # Séparateur
        tk.Frame(body, bg=self.colors['border'], height=1).pack(fill=tk.X, pady=5)
        
        # Boutons batterie
        battery_frame = tk.Frame(body, bg=self.colors['bg_secondary'])
        battery_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(battery_frame, text="🔋 Battery:",
                font=('Segoe UI', 9, 'bold'),
                bg=self.colors['bg_secondary'],
                fg=self.colors['accent_green']).pack(anchor='w')
        
        battery_btns = tk.Frame(battery_frame, bg=self.colors['bg_secondary'])
        battery_btns.pack(fill=tk.X, padx=10, pady=2)
        
        self.create_scenario_button(battery_btns, "⚠️ Batterie Faible", "low_battery", self.colors['accent_orange'])
        self.create_scenario_button(battery_btns, "🚨 Critique", "critical_battery", self.colors['accent_red'])
        
        # Séparateur
        tk.Frame(body, bg=self.colors['border'], height=1).pack(fill=tk.X, pady=5)
        
        # Boutons présence
        presence_frame = tk.Frame(body, bg=self.colors['bg_secondary'])
        presence_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(presence_frame, text="👥 Presence:",
                font=('Segoe UI', 9, 'bold'),
                bg=self.colors['bg_secondary'],
                fg=self.colors['accent_purple']).pack(anchor='w')
        
        presence_btns = tk.Frame(presence_frame, bg=self.colors['bg_secondary'])
        presence_btns.pack(fill=tk.X, padx=10, pady=2)
        
        self.create_scenario_button(presence_btns, "👥 Présence", "presence_detected", self.colors['accent_green'])
        self.create_scenario_button(presence_btns, "🚶 Absence", "no_presence", self.colors['text_secondary'])
    
    def create_events_journal(self, parent, row, col, rowspan=1):
        """Crée le journal d'événements en haut à droite avec coins arrondis"""
        # Container avec effet d'ombre et coins arrondis simulés
        shadow_frame = tk.Frame(parent, bg='#0a0a0a', relief='flat')
        shadow_frame.grid(row=row, column=col, rowspan=rowspan, padx=15, pady=15, sticky='nsew')
        
        # Frame principale avec coins arrondis simulés
        card = tk.Frame(shadow_frame, bg=self.colors['bg_secondary'], relief='flat')
        card.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # Appliquer coins arrondis
        self.create_rounded_corners(card)
        
        # En-tête avec dégradé simulé
        header_container = tk.Frame(card, bg=self.colors['bg_secondary'])
        header_container.pack(fill=tk.X, padx=8, pady=(8, 0))
        
        # Header principal
        header = tk.Frame(header_container, bg=self.colors['accent_red'], height=45)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        title_frame = tk.Frame(header, bg=self.colors['accent_red'])
        title_frame.pack(expand=True, fill=tk.BOTH)
        
        title = tk.Label(title_frame, text="📜 JOURNAL DES ÉVÉNEMENTS",
                        font=('Segoe UI', 12, 'bold'),
                        bg=self.colors['accent_red'],
                        fg='white')
        title.pack(side=tk.LEFT, padx=15, pady=12)
        
        # Indicateur de statut en temps réel
        self.journal_status = tk.Label(title_frame, text="🟢 ACTIF",
                                      font=('Segoe UI', 9, 'bold'),
                                      bg=self.colors['accent_red'],
                                      fg='white')
        self.journal_status.pack(side=tk.RIGHT, padx=15, pady=12)
        
        # Corps du journal
        body = tk.Frame(card, bg=self.colors['bg_secondary'])
        body.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)
        
        # Header des statistiques
        stats_frame = tk.Frame(body, bg=self.colors['bg_accent'], height=35)
        stats_frame.pack(fill=tk.X, pady=(0, 8))
        stats_frame.pack_propagate(False)
        
        self.events_counter = tk.Label(stats_frame, 
                                      text="📊 Événements: 0",
                                      font=('Segoe UI', 9, 'bold'),
                                      bg=self.colors['bg_accent'],
                                      fg=self.colors['text_primary'])
        self.events_counter.pack(side=tk.LEFT, padx=12, pady=8)
        
        self.last_event_time = tk.Label(stats_frame, 
                                       text="⏰ Dernier: --:--:--",
                                       font=('Segoe UI', 9),
                                       bg=self.colors['bg_accent'],
                                       fg=self.colors['text_secondary'])
        self.last_event_time.pack(side=tk.RIGHT, padx=12, pady=8)
        
        # Zone de texte avec fond très contrasté
        text_container = tk.Frame(body, bg=self.colors['bg_secondary'])
        text_container.pack(fill=tk.BOTH, expand=True)
        
        self.alarms_text = scrolledtext.ScrolledText(
            text_container,
            height=20,  # Plus haut pour être visible
            font=('Consolas', 10, 'bold'),
            bg='#0d1117',  # Fond GitHub-like
            fg='#58a6ff',  # Texte bleu clair
            insertbackground='#58a6ff',
            selectbackground=self.colors['accent_blue'],
            selectforeground='white',
            wrap=tk.WORD,
            relief='flat',
            borderwidth=0,
            padx=8,
            pady=8
        )
        self.alarms_text.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)
        
        # Configuration des tags de couleur
        self.alarms_text.tag_config("INFO", foreground="#7dd3fc")
        self.alarms_text.tag_config("WARNING", foreground="#fbbf24")
        self.alarms_text.tag_config("ERROR", foreground="#f87171")
        self.alarms_text.tag_config("SUCCESS", foreground="#4ade80")
        self.alarms_text.tag_config("SCENARIO", foreground="#c084fc")
        self.alarms_text.tag_config("SYSTEM", foreground="#60a5fa")
        self.alarms_text.tag_config("SENSOR", foreground="#34d399")
        self.alarms_text.tag_config("ACTION", foreground="#fbbf24", font=('Consolas', 10, 'bold'))
        
        # Initialiser
        self.event_count = 0
        
        # Messages de démarrage
        self.log_event("🚀 SYSTÈME DE MONITORING DÉMARRÉ", "SUCCESS")
        self.log_event("📡 Initialisation modules Climate, Presence, Battery", "INFO")
        self.log_event("📊 Interface HMI prête - Surveillance active", "INFO")
        self.log_event("="*50, "INFO", False)
    
    def create_rounded_corners(self, parent):
        """Simule des coins arrondis avec des mini-frames"""
        corner_size = 8
        corner_color = self.colors['bg_primary']  # Couleur de fond pour simuler arrondis
        
        # Coins supérieurs
        top_left = tk.Frame(parent, bg=corner_color, width=corner_size, height=corner_size)
        top_left.place(x=0, y=0)
        
        top_right = tk.Frame(parent, bg=corner_color, width=corner_size, height=corner_size)
        top_right.place(relx=1.0, x=-corner_size, y=0)
        
        # Coins inférieurs
        bottom_left = tk.Frame(parent, bg=corner_color, width=corner_size, height=corner_size)
        bottom_left.place(x=0, rely=1.0, y=-corner_size)
        
        bottom_right = tk.Frame(parent, bg=corner_color, width=corner_size, height=corner_size)
        bottom_right.place(relx=1.0, x=-corner_size, rely=1.0, y=-corner_size)
    
    def create_alarms_panel(self, parent, row, col, colspan=1):
        """Crée le panel d'alarmes moderne"""
        # Container avec effet d'ombre simulé
        shadow_frame = tk.Frame(parent, bg='#0a0a0a', relief='flat')
        shadow_frame.grid(row=row, column=col, columnspan=colspan, padx=12, pady=12, sticky='ew')
        
        card = tk.Frame(shadow_frame, bg=self.colors['bg_secondary'], relief='flat')
        card.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # En-tête
        header = tk.Frame(card, bg=self.colors['accent_red'], height=40)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        title = tk.Label(header, text="🚨 JOURNAL DES ÉVÉNEMENTS",
                        font=('Segoe UI', 12, 'bold'),
                        bg=self.colors['accent_red'],
                        fg='white')
        title.pack(pady=10)
        
        # Zone de texte avec style sombre amélioré
        text_frame = tk.Frame(card, bg=self.colors['bg_secondary'])
        text_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Header du journal avec statistiques
        journal_header = tk.Frame(text_frame, bg=self.colors['bg_accent'], height=30)
        journal_header.pack(fill=tk.X, pady=(0, 5))
        journal_header.pack_propagate(False)
        
        self.events_counter = tk.Label(journal_header, 
                                      text="📊 Événements: 0",
                                      font=('Segoe UI', 9, 'bold'),
                                      bg=self.colors['bg_accent'],
                                      fg=self.colors['text_primary'])
        self.events_counter.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.last_event_time = tk.Label(journal_header, 
                                       text="⏰ Dernier: --:--:--",
                                       font=('Segoe UI', 9),
                                       bg=self.colors['bg_accent'],
                                       fg=self.colors['text_secondary'])
        self.last_event_time.pack(side=tk.RIGHT, padx=10, pady=5)
        
        # Zone de texte principale plus grande et visible
        self.alarms_text = scrolledtext.ScrolledText(
            text_frame,
            height=12,  # Plus grand pour plus de visibilité
            font=('Consolas', 11, 'bold'),  # Police plus grande et en gras
            bg='#0d1117',  # Fond très sombre pour contraste
            fg='#58a6ff',  # Bleu clair pour le texte
            insertbackground='#58a6ff',
            selectbackground=self.colors['accent_blue'],
            selectforeground='white',
            wrap=tk.WORD,
            relief='flat',
            borderwidth=0
        )
        self.alarms_text.pack(fill=tk.BOTH, expand=True)
        
        # Configuration des tags de couleur pour différents types d'événements
        self.alarms_text.tag_config("INFO", foreground="#7dd3fc")     # Bleu clair pour info
        self.alarms_text.tag_config("WARNING", foreground="#fbbf24")  # Jaune pour warnings
        self.alarms_text.tag_config("ERROR", foreground="#f87171")    # Rouge pour erreurs
        self.alarms_text.tag_config("SUCCESS", foreground="#4ade80")  # Vert pour succès
        self.alarms_text.tag_config("SCENARIO", foreground="#c084fc") # Violet pour scénarios
        self.alarms_text.tag_config("TIMESTAMP", foreground="#9ca3af") # Gris pour timestamps
        
        # Initialiser le compteur d'événements
        self.event_count = 0
        
        # Message de bienvenue dans le journal
        self.log_event("🚀 SYSTÈME DE MONITORING DÉMARRÉ", "INFO")
        self.log_event("📡 Modules Climate, Presence, Battery initialisés", "SUCCESS")
        self.log_event("🎮 Interface HMI prête - Utilisez les boutons pour tester", "INFO")
    
    def create_metric_widget(self, parent, label_text, var_name, unit, color):
        """Crée un widget de métrique moderne"""
        frame = tk.Frame(parent, bg=self.colors['bg_secondary'])
        
        # Conteneur pour l'alignement
        container = tk.Frame(frame, bg=self.colors['bg_secondary'])
        container.pack(fill=tk.X, pady=2)
        
        # Label de la métrique
        label = tk.Label(container, text=label_text,
                        font=('Segoe UI', 9, 'bold'),
                        bg=self.colors['bg_secondary'],
                        fg=self.colors['text_secondary'])
        label.pack(side=tk.LEFT)
        
        # Valeur avec unité
        if var_name not in self.status_vars:
            self.status_vars[var_name] = tk.StringVar(value="--")
        
        value_frame = tk.Frame(container, bg=self.colors['bg_secondary'])
        value_frame.pack(side=tk.RIGHT)
        
        value_label = tk.Label(value_frame,
                              textvariable=self.status_vars[var_name],
                              font=('Consolas', 12, 'bold'),
                              bg=self.colors['bg_secondary'],
                              fg=color)
        value_label.pack(side=tk.LEFT)
        
        unit_label = tk.Label(value_frame, text=unit,
                             font=('Segoe UI', 9),
                             bg=self.colors['bg_secondary'],
                             fg=self.colors['text_secondary'])
        unit_label.pack(side=tk.LEFT, padx=(2, 0))
        
        return frame
    
    def create_actuator_status(self, parent, label_text, led_var, status_var):
        """Crée un indicateur d'état d'actionneur avec LED"""
        frame = tk.Frame(parent, bg=self.colors['bg_secondary'])
        frame.pack(fill=tk.X, pady=3)
        
        # Label de l'actionneur
        label = tk.Label(frame, text=label_text,
                        font=('Segoe UI', 10),
                        bg=self.colors['bg_secondary'],
                        fg=self.colors['text_secondary'])
        label.pack(side=tk.LEFT)
        
        # Container pour LED + status
        status_container = tk.Frame(frame, bg=self.colors['bg_secondary'])
        status_container.pack(side=tk.RIGHT)
        
        # LED indicator
        if led_var not in self.status_vars:
            self.status_vars[led_var] = tk.StringVar(value="🔴")
        
        led_label = tk.Label(status_container,
                            textvariable=self.status_vars[led_var],
                            font=('Segoe UI', 14),
                            bg=self.colors['bg_secondary'])
        led_label.pack(side=tk.LEFT, padx=(0, 5))
        
        # Status text
        if status_var not in self.status_vars:
            self.status_vars[status_var] = tk.StringVar(value="OFF")
        
        status_label = tk.Label(status_container,
                               textvariable=self.status_vars[status_var],
                               font=('Segoe UI', 10, 'bold'),
                               bg=self.colors['bg_secondary'],
                               fg=self.colors['text_primary'])
        status_label.pack(side=tk.LEFT)
    
    def create_scenario_button(self, parent, text, scenario_name, color):
        """Crée un bouton de scénario moderne"""
        btn = tk.Button(parent, text=text,
                       font=('Segoe UI', 8, 'bold'),
                       bg=color,
                       fg='white',
                       activebackground=self._darken_color(color),
                       activeforeground='white',
                       relief='flat',
                       borderwidth=0,
                       padx=8,
                       pady=4,
                       cursor='hand2',
                       command=lambda: self.trigger_scenario(scenario_name))
        btn.pack(side=tk.LEFT, padx=2, pady=1)
        
        # Effet hover
        def on_enter(e):
            btn.configure(bg=self._darken_color(color))
        
        def on_leave(e):
            btn.configure(bg=color)
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
    
    def _darken_color(self, color):
        """Assombrit une couleur hexadécimale"""
        # Conversion simple pour effet hover
        color_map = {
            self.colors['accent_blue']: '#005580',
            self.colors['accent_red']: '#d32f2f',
            self.colors['accent_green']: '#388e3c',
            self.colors['accent_orange']: '#f57c00',
            self.colors['accent_purple']: '#7b1fa2',
            self.colors['text_secondary']: '#909090'
        }
        return color_map.get(color, '#404040')
    
    def trigger_scenario(self, scenario_name):
        """Déclenche manuellement un scénario avec logging détaillé"""
        if scenario_name in SCENARIOS:
            scenario = SCENARIOS[scenario_name]
            duration = scenario['duration']
            
            # Messages détaillés selon le scénario
            scenario_descriptions = {
                'high_temperature': f'🔥 SIMULATION: Température élevée (32°C) pendant {duration}s - Test ventilation',
                'low_temperature': f'❄️ SIMULATION: Température basse (22°C) pendant {duration}s - Test chauffage',
                'high_co2': f'💨 SIMULATION: CO₂ élevé (1200ppm) pendant {duration}s - Test ventilation forcée',
                'low_battery': f'🔋 SIMULATION: Batterie faible (10.5V) pendant {duration}s - Test alertes',
                'critical_battery': f'⚡ SIMULATION: Batterie critique (9.8V) pendant {duration}s - Test mode économie',
                'presence_detected': f'👥 SIMULATION: Présence détectée (3 pers.) pendant {duration}s - Test éclairage',
                'no_presence': f'🚫 SIMULATION: Absence totale pendant {duration}s - Test extinction auto'
            }
            
            description = scenario_descriptions.get(scenario_name, f'Scénario {scenario_name}')
            self.log_event(description, "SCENARIO")
            
            # Déclencher le scénario dans le bon module
            if scenario_name in ['high_temperature', 'low_temperature', 'high_co2']:
                self.climate_module.force_scenario(scenario_name, duration)
                self.log_event(f"🌡️ Module Climate: Scénario '{scenario_name}' actif", "SYSTEM")
            elif scenario_name in ['presence_detected', 'no_presence']:
                self.presence_module.force_scenario(scenario_name, duration)
                self.log_event(f"👥 Module Presence: Scénario '{scenario_name}' actif", "SYSTEM")
            elif scenario_name in ['low_battery', 'critical_battery']:
                self.battery_module.force_scenario(scenario_name, duration)
                self.log_event(f"🔋 Module Battery: Scénario '{scenario_name}' actif", "SYSTEM")
            
            # Logger la fin programée du scénario
            end_time = time.strftime("%H:%M:%S", time.localtime(time.time() + duration))
            self.log_event(f"⏰ Scénario se terminera automatiquement à {end_time}", "INFO")
    
    def update_display(self):
        """Met à jour l'affichage avec les nouvelles valeurs"""
        # Mettre à jour Climate
        climate_status = self.climate_module.get_status()
        
        # Nouvelles variables pour le design moderne
        if 'temp_display' in self.status_vars:
            self.status_vars['temp_display'].set(str(climate_status['temperature']))
        if 'humidity_display' in self.status_vars:
            self.status_vars['humidity_display'].set(str(climate_status['humidity']))
        if 'co2_display' in self.status_vars:
            self.status_vars['co2_display'].set(str(climate_status['co2']))
        
        # LEDs et statuts des actionneurs
        if 'ventilator_led' in self.status_vars:
            self.status_vars['ventilator_led'].set("🟢" if climate_status['ventilator_on'] else "🔴")
        if 'ventilator_status' in self.status_vars:
            self.status_vars['ventilator_status'].set("ON" if climate_status['ventilator_on'] else "OFF")
        
        if 'forced_vent_led' in self.status_vars:
            self.status_vars['forced_vent_led'].set("🟡" if climate_status['forced_ventilation'] else "🔴")
        if 'forced_vent_status' in self.status_vars:
            self.status_vars['forced_vent_status'].set("FORCÉE" if climate_status['forced_ventilation'] else "NORMAL")
        
        # Mettre à jour Presence
        presence_status = self.presence_module.get_status()
        
        if 'movement_indicator' in self.status_vars:
            self.status_vars['movement_indicator'].set("✅" if presence_status['movement_detected'] else "❌")
        
        if 'persons_display' in self.status_vars:
            self.status_vars['persons_display'].set(str(presence_status['persons_count']))
        
        time_since = presence_status['time_since_movement']
        if 'time_since_display' in self.status_vars:
            self.status_vars['time_since_display'].set(str(int(time_since)) if time_since else "--")
        
        if 'lights_led' in self.status_vars:
            self.status_vars['lights_led'].set("🟡" if presence_status['lights_on'] else "🔴")
        if 'lights_status' in self.status_vars:
            self.status_vars['lights_status'].set("ON" if presence_status['lights_on'] else "OFF")
        
        # Mettre à jour Battery
        battery_status = self.battery_module.get_status()
        
        if 'voltage_display' in self.status_vars:
            self.status_vars['voltage_display'].set(str(battery_status['voltage']))
        if 'current_display' in self.status_vars:
            self.status_vars['current_display'].set(str(battery_status['current']))
        if 'battery_temp_display' in self.status_vars:
            self.status_vars['battery_temp_display'].set(str(battery_status['temperature']))
        
        # Capacité avec icône dynamique
        if 'capacity_bar' in self.status_vars:
            capacity = battery_status['capacity_percent']
            self.status_vars['capacity_bar'].set(f"{capacity}%")
            
            # Icône batterie selon la capacité
            if 'battery_icon' in self.status_vars:
                if capacity > 75:
                    self.status_vars['battery_icon'].set("🔋")
                elif capacity > 50:
                    self.status_vars['battery_icon'].set("🔋")
                elif capacity > 25:
                    self.status_vars['battery_icon'].set("🪫")
                else:
                    self.status_vars['battery_icon'].set("🪫")
        
        # Statuts système avec LEDs
        if 'battery_status_led' in self.status_vars:
            status_leds = {
                'Normal': '🟢',
                'Low': '🟡', 
                'Critical': '🟠',
                'Shutdown': '🔴'
            }
            self.status_vars['battery_status_led'].set(status_leds.get(battery_status['battery_status'], '🔴'))
        
        if 'battery_status_text' in self.status_vars:
            self.status_vars['battery_status_text'].set(battery_status['battery_status'].upper())
        
        if 'power_save_led' in self.status_vars:
            self.status_vars['power_save_led'].set("🟡" if battery_status['power_save_mode'] else "🔴")
        if 'power_save_text' in self.status_vars:
            self.status_vars['power_save_text'].set("ACTIVÉ" if battery_status['power_save_mode'] else "DÉSACTIVÉ")
        
        # Mettre à jour l'horloge
        current_time = time.strftime("%H:%M:%S")
        self.system_clock.configure(text=current_time)
        
        # Mettre à jour l'indicateur système global avec plus de détails
        total_alarms = len(self.climate_module.get_alarms()) + len(self.presence_module.get_alarms()) + len(self.battery_module.get_alarms())
        
        if battery_status['battery_status'] == 'Shutdown':
            self.system_status.configure(text="💀 SYSTÈME ARRÊT", fg=self.colors['accent_red'])
        elif battery_status['battery_status'] == 'Critical':
            self.system_status.configure(text="⚡ SYSTÈME CRITIQUE", fg=self.colors['accent_red'])
        elif total_alarms > 2:
            self.system_status.configure(text=f"🚨 {total_alarms} ALERTES", fg=self.colors['accent_red'])
        elif total_alarms > 0:
            self.system_status.configure(text=f"🟡 {total_alarms} ALERTE(S)", fg=self.colors['accent_orange'])
        elif any([climate_status['scenario_active'], presence_status['scenario_active'], battery_status['scenario_active']]):
            self.system_status.configure(text="🎭 SCÉNARIO ACTIF", fg=self.colors['accent_purple'])
        else:
            self.system_status.configure(text="🟢 SYSTÈME ACTIF", fg=self.colors['accent_green'])
        
        # Mettre à jour les alarmes
        self.update_alarms()
        
        # Programmer la prochaine mise à jour
        self.root.after(HMI_CONFIG['refresh_rate'], self.update_display)
    
    def update_alarms(self):
        """Met à jour la section des alarmes et log les événements détaillés"""
        # Récupérer les statuts actuels
        climate_status = self.climate_module.get_status()
        presence_status = self.presence_module.get_status()
        battery_status = self.battery_module.get_status()
        
        # Logger les changements d'état importants
        if hasattr(self, 'previous_states'):
            # Vérifier les changements Climate
            if climate_status['ventilator_on'] != self.previous_states['ventilator_on']:
                state = "ACTIVÉ" if climate_status['ventilator_on'] else "DÉSACTIVÉ"
                self.log_event(f"🌪️ Ventilateur {state} (Temp: {climate_status['temperature']}°C)", "SYSTEM")
            
            if climate_status['forced_ventilation'] != self.previous_states['forced_ventilation']:
                state = "ACTIVÉE" if climate_status['forced_ventilation'] else "DÉSACTIVÉE"
                self.log_event(f"💨 Ventilation forcée {state} (CO₂: {climate_status['co2']} ppm)", "SYSTEM")
            
            # Vérifier les changements Presence
            if presence_status['lights_on'] != self.previous_states['lights_on']:
                state = "ALLUMÉES" if presence_status['lights_on'] else "ÉTEINTES"
                persons = presence_status['persons_count']
                self.log_event(f"💡 Éclairage {state} ({persons} personne(s) détectée(s))", "SYSTEM")
            
            if presence_status['movement_detected'] and not self.previous_states.get('movement_detected', False):
                self.log_event(f"🚪 Mouvement détecté - {presence_status['persons_count']} personne(s)", "SENSOR")
            
            # Vérifier les changements Battery
            if battery_status['battery_status'] != self.previous_states['battery_status']:
                voltage = battery_status['voltage']
                if battery_status['battery_status'] == 'Critical':
                    self.log_event(f"⚡ BATTERIE CRITIQUE! Tension: {voltage}V - Mode économie activé", "ERROR")
                elif battery_status['battery_status'] == 'Low':
                    self.log_event(f"🔋 Batterie faible - Tension: {voltage}V", "WARNING")
                elif battery_status['battery_status'] == 'Normal':
                    self.log_event(f"✅ Batterie revenue à la normale - Tension: {voltage}V", "SUCCESS")
        
        # Récupérer et logger les alarmes actuelles
        climate_alarms = self.climate_module.get_alarms()
        presence_alarms = self.presence_module.get_alarms()
        battery_alarms = self.battery_module.get_alarms()
        
        # Logger les nouvelles alarmes uniquement
        all_current_alarms = climate_alarms + presence_alarms + battery_alarms
        
        if hasattr(self, 'previous_alarms'):
            new_alarms = [alarm for alarm in all_current_alarms if alarm not in self.previous_alarms]
            for alarm in new_alarms:
                if "température" in alarm.lower():
                    self.log_event(f"🌡️ {alarm}", "WARNING")
                elif "co₂" in alarm.lower():
                    self.log_event(f"💨 {alarm}", "WARNING")
                elif "batterie" in alarm.lower():
                    self.log_event(f"🔋 {alarm}", "ERROR" if "critique" in alarm.lower() else "WARNING")
                elif "lampe" in alarm.lower():
                    self.log_event(f"💡 {alarm}", "WARNING")
                else:
                    self.log_event(alarm, "WARNING")
        
        # Sauvegarder les états pour la prochaine comparaison
        self.previous_states = {
            'ventilator_on': climate_status['ventilator_on'],
            'forced_ventilation': climate_status['forced_ventilation'],
            'lights_on': presence_status['lights_on'],
            'movement_detected': presence_status['movement_detected'],
            'battery_status': battery_status['battery_status']
        }
        self.previous_alarms = all_current_alarms
        
        # Logger des métriques périodiques (toutes les 30 secondes)
        if not hasattr(self, 'last_metrics_log'):
            self.last_metrics_log = 0
        
        current_time = time.time()
        if current_time - self.last_metrics_log > 30:  # Toutes les 30 secondes
            self.log_event(f"📊 Métriques: Temp={climate_status['temperature']}°C, CO₂={climate_status['co2']}ppm, Batterie={battery_status['voltage']}V", "SENSOR")
            self.last_metrics_log = current_time
    
    def log_event(self, message, event_type="INFO", show_timestamp=True):
        """Ajoute un événement au journal avec style et couleurs"""
        current_time = time.strftime("%H:%M:%S")
        
        # Icônes selon le type d'événement
        icons = {
            "INFO": "🟦",
            "WARNING": "⚠️",
            "ERROR": "🔴",
            "SUCCESS": "✅",
            "SCENARIO": "🎭",
            "SYSTEM": "⚙️",
            "SENSOR": "📈"
        }
        
        icon = icons.get(event_type, "🟦")
        
        # Construction du message avec formatage
        if show_timestamp:
            formatted_message = f"[{current_time}] {icon} {message}\n"
        else:
            formatted_message = f"{icon} {message}\n"
        
        # Insérer le message avec les tags de couleur
        start_pos = self.alarms_text.index(tk.END)
        self.alarms_text.insert(tk.END, formatted_message)
        
        # Appliquer le tag de couleur au message complet
        line_start = f"{start_pos.split('.')[0]}.0"
        line_end = f"{int(start_pos.split('.')[0])}.end"
        self.alarms_text.tag_add(event_type, line_start, line_end)
        
        # Faire défiler vers le bas
        self.alarms_text.see(tk.END)
        
        # Mettre à jour les statistiques
        self.event_count += 1
        self.events_counter.configure(text=f"📊 Événements: {self.event_count}")
        self.last_event_time.configure(text=f"⏰ Dernier: {current_time}")
        
        # Garder seulement les 150 dernières lignes pour éviter la surcharge
        lines = self.alarms_text.get("1.0", tk.END).split("\n")
        if len(lines) > 150:
            # Supprimer les anciennes lignes
            lines_to_remove = len(lines) - 150
            self.alarms_text.delete("1.0", f"{lines_to_remove}.0")
    
    def log_alarm(self, message):
        """Fonction de compatibilité - utilise le nouveau système"""
        # Déterminer le type selon le contenu
        if "scenario" in message.lower() or "scénario" in message.lower():
            self.log_event(message, "SCENARIO")
        elif "alerte" in message.lower() or "alarme" in message.lower():
            self.log_event(message, "WARNING")
        elif "critique" in message.lower() or "erreur" in message.lower():
            self.log_event(message, "ERROR")
        elif "succès" in message.lower() or "terminé" in message.lower():
            self.log_event(message, "SUCCESS")
        else:
            self.log_event(message, "INFO")
