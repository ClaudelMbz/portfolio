import React, { useState, useEffect } from 'react';
import { Menu, X, Download, Github, Linkedin, Mail, ChevronRight, ExternalLink } from 'lucide-react';

import avatarImg from '/avatar.jpg';
import cs50xImg from '/CS50x.png';
import cs50aiImg from '/CS50AI.png';
import awsImg from '/awsbnbrunners.jpg';

const Portfolio = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [activeSection, setActiveSection] = useState('bio');
  const [language, setLanguage] = useState('en');

  const content = {
    en: {
      nav: {
        bio: 'Bio',
        papers: 'Papers',
        talks: 'Talks',
        news: 'News',
        experience: 'Experience',
        projects: 'Projects',
        teaching: 'Teaching'
      },
      hero: {
        name: 'Claudel Mubenzem',
        title: 'Aspiring AI & Automation Engineer',
        status: '🔧 Engineering Student',
        downloadCV: 'Download CV'
      },
      about: {
        title: 'My Engineering & AI Automation Work',
        description: 'Welcome to my portfolio! I am an engineering student and aspiring AI & Automation Engineer, passionate about transforming raw data into concrete operational solutions.\n\nMy expertise includes industrial data analysis, workflow design and automation, AI agent development, and producing actionable MVPs from raw ideas. My approach is simple: I take an idea, quickly prototype it, test it with concrete feedback, and deliver a functional MVP.\n\nI am always ready to collaborate on innovative projects combining AI, automation, and data engineering to make a real impact! 🌟'
      },
      interests: {
        title: 'Interests',
        items: [
          'AI & Machine Learning (RAG, Agents, Prompting)',
          'Industrial Data & Process Optimization',
          'Gen AI Tools',
          'Automation & Productive Workflows',
          'Technical documentation (PRD) & product-ready systems'
        ]
      },
      experience: {
        title: 'Experience',
        jobs: [
          {
            role: 'Data Analyst and Industrial Implementation',
            company: 'DBD SARL',
            period: 'June 2025 - August 2025',
            description: 'Design reproducible factory models integrating costs, pricing, logistics, machinery and resources. Write detailed technical documents (PRD) to facilitate field implementation. Analyze industrial data to support strategic decisions and validate profitability. Optimize operational performance through analysis and modeling. Ensure the link between technical documentation, industrial strategy and data analysis.'
          },
          {
            role: 'Assistant Electrical Technician',
            company: 'Universal Project Consulting',
            period: 'January 2024 - March 2024',
            description: 'Air conditioning systems installation, fire safety, photovoltaic'
          }
        ]
      },
      education: {
        title: 'Education',
        items: [
          {
            degree: 'Bachelor of Science (B.Sc.) in Engineering',
            institution: 'ICAM',
            period: 'September 2025 - August 2026',
            specialization: 'General Engineering Track',
            courses: [
              'Python (Programming Language)',
              'Risk Management',
              'Unified Modeling Language (UML)',
              'Operations Research',
              'Problem Solving',
              'Data Modeling',
              '3D Modeling',
              'Continuous Improvement',
              'French',
              'English'
            ]
          },
          {
            degree: 'Bachelor of Science (B.Sc.) in Engineering',
            institution: 'Faculté d\'ingénierie ULC-Icam',
            period: 'September 2022 - June 2025',
            specialization: 'General polytechnic track (Computer Science, Mathematics & Communications)',
            courses: [
  'Conception électronique',
  'Modélisation 3D',
  'Résolution de problèmes',
  'Résolution de problèmes par analyse des causes profondes',
  'Programmation',
  'Python (langage de programmation)',
  'Schémas électriques',
  'Analyse fonctionnelle',
  'Documentation technique',
  'Sens de l’organisation',
  'Travail d’équipe',
]
          },
          {
            degree: 'Mathematics and Physics',
            institution: 'Collège Bonsomi',
            period: 'September 2016 - September 2022'
          }
        ]
      },
      skills: {
        title: 'Skills & Expertise',
        items: [
          { name: 'AI & Machine Learning', level: 80, desc: 'RAG pipelines, LlamaIndex, Ollama' },
          { name: 'Python Development', level: 90, desc: 'FastAPI, automation, web scraping' },
          { name: 'JavaScript & Extensions', level: 85, desc: 'Chrome APIs, web development' },
          { name: 'Data Analysis', level: 85, desc: 'Process optimization & insights' },
          { name: 'Database Systems', level: 80, desc: 'MongoDB, PostgreSQL, Qdrant' },
          { name: 'Technical Documentation', level: 90, desc: 'PRD writing, specifications' },
          { name: 'Project Management', level: 75, desc: 'Team coordination, implementation' },
          { name: 'DevOps & Automation', level: 75, desc: 'Docker, n8n workflows' }
        ]
      },
      projects: {
        title: 'Selected Projects',
        subtitle: 'I enjoy making things. Here are a selection of projects that I have worked on over the years.',
        items: [
          {
            title: 'Job Finder Bot & Scraper',
            description: 'A complete job-finding solution with web scraping and Telegram bot integration. Features AI-powered job summarization using Mistral AI, MongoDB storage, and automated job delivery to users.',
            link: 'https://github.com/ClaudelMbz/jobFinder',
            tags: ['Python', 'Telegram Bot', 'Web Scraping', 'AI', 'MongoDB']
          },
          {
            title: 'PromptForge',
            description: 'A browser extension that supercharges interactions with Large Language Models. Features prompt optimization algorithms (Primer & Mastermind), seamless integration with ChatGPT, Gemini, and DeepSeek.',
            link: 'https://github.com/ClaudelMbz/PromptForge-SPEA-',
            tags: ['JavaScript', 'Chrome Extension', 'AI', 'LLM', 'Browser Extension']
          },
          {
            title: 'Job Scraping System',
            description: 'Advanced web scraping system for job postings with AI integration. Automates job discovery, processing, and storage with intelligent data extraction and summarization capabilities.',
            link: 'https://github.com/ClaudelMbz/jobScraping',
            tags: ['Python', 'Web Scraping', 'Data Processing', 'Automation', 'AI']
          }
        ]
      },
      certifications: {
        title: 'Certifications',
        items: [
          {
            name: 'CS50x - Introduction to Computer Science',
            institution: 'Harvard University',
            date: 'December 2023',
            link: null,
            image: cs50xImg,
            download: false
          },
          {
            name: 'CS50 Introduction to Artificial Intelligence with Python',
            institution: 'Harvard University',
            date: 'March 2024',
            link: null,
            image: cs50aiImg,
            download: false
          },
          {
            name: 'AWS BNB Node Runners',
            institution: 'Amazon Web Services',
            date: 'January 2024',
            link: null,
            image: awsImg,
            download: false
          }
        ]
      }
    },
    fr: {
      nav: {
        bio: 'Bio',
        papers: 'Publications',
        talks: 'Conférences',
        news: 'Actualités',
        experience: 'Expérience',
        projects: 'Projets',
        teaching: 'Enseignement'
      },
      hero: {
        name: 'Claudel Mubenzem',
        title: 'Ingénieur IA & Automatisation en devenir',
        status: '🔧 Étudiant en Ingénierie',
        downloadCV: 'Télécharger CV'
      },
      about: {
        title: 'Mon Travail en Ingénierie IA & Automatisation',
        description: 'Bienvenue sur mon portfolio ! Je suis étudiant en ingénierie et futur ingénieur IA & Automatisation, passionné par la transformation de données brutes en solutions opérationnelles concrètes.\n\nMon expertise comprend l\'analyse de données industrielles, la conception et l\'automatisation de workflows, le développement d\'agents IA, et la production de MVP actionnables à partir d\'idées brutes. Mon approche est simple : je prends une idée, la prototypage rapidement, la teste avec des retours concrets, et livre un MVP fonctionnel.\n\nJe suis toujours prêt à collaborer sur des projets innovants combinant IA, automatisation et ingénierie des données pour avoir un impact réel ! 🌟'
      },
      interests: {
        title: 'Centres d\'intérêt',
        items: [
          'IA & Machine Learning (RAG, Agents, Prompting)',
          'Données Industrielles & Optimisation de Processus',
          'Outils d\'IA Générative',
          'Automatisation & Workflows Productifs',
          'Documentation technique (PRD) & systèmes prêts pour la production'
        ]
      },
      experience: {
        title: 'Expérience',
        jobs: [
          {
            role: 'Analyste de Données et Implémentation Industrielle',
            company: 'DBD SARL',
            period: 'Juin 2025 - Août 2025',
            description: 'Concevoir des modèles d\'usines reproductibles intégrant coûts, prix, logistique, machines et ressources. Rédiger des documents techniques détaillés (PRD) pour faciliter la mise en œuvre terrain. Analyser les données industrielles pour appuyer les décisions stratégiques et valider la rentabilité. Optimiser les performances opérationnelles via l\'analyse et la modélisation. Assurer le lien entre documentation technique, stratégie industrielle et data analysis.'
          },
          {
            role: 'Technicien Électricien Assistant',
            company: 'Universal Project Consulting',
            period: 'Janvier 2024 - Mars 2024',
            description: 'Installation systèmes climatisation, sécurité incendie, photovoltaïque'
          }
        ]
      },
      education: {
        title: 'Formation',
        items: [
          {
            degree: 'Licence en Sciences de l\'Ingénieur (B.Sc.)',
            institution: 'ICAM',
            period: 'Septembre 2025 - Août 2026',
            specialization: 'Parcours Ingénierie Générale',
            courses: [
              'Python (langage de programmation)',
              'Gestion des risques',
              'Langage de modélisation unifié (UML)',
              'Recherche opérationnelle',
              'Problem Solving',
              'Modélisation des données',
              'Modélisation 3D',
              'Amélioration continue',
              'Français',
              'English'
            ]
          },
          {
            degree: 'Licence en Sciences de l\'Ingénieur (B.Sc.)',
            institution: 'Faculté d\'ingénierie ULC-Icam',
            period: 'Septembre 2022 - Juin 2025',
            specialization: 'Parcours polytechnique général (Informatique, Mathématiques & Communications)'
          },
          {
            degree: 'Mathématiques et Physique',
            institution: 'Collège Bonsomi',
            period: 'Septembre 2016 - Septembre 2022'
          }
        ]
      },
      skills: {
        title: 'Compétences & Expertise',
        items: [
          { name: 'IA & Machine Learning', level: 80, desc: 'Pipelines RAG, LlamaIndex, Ollama' },
          { name: 'Développement Python', level: 90, desc: 'FastAPI, automatisation, web scraping' },
          { name: 'JavaScript & Extensions', level: 85, desc: 'APIs Chrome, développement web' },
          { name: 'Analyse de Données', level: 85, desc: 'Optimisation de processus & insights' },
          { name: 'Systèmes de Bases de Données', level: 80, desc: 'MongoDB, PostgreSQL, Qdrant' },
          { name: 'Documentation Technique', level: 90, desc: 'Rédaction PRD, spécifications' },
          { name: 'Gestion de Projet', level: 75, desc: 'Coordination d\'équipe, implémentation' },
          { name: 'DevOps & Automatisation', level: 75, desc: 'Docker, workflows n8n' }
        ]
      },
      projects: {
        title: 'Projets Sélectionnés',
        subtitle: 'J\'aime créer des choses. Voici une sélection de projets sur lesquels j\'ai travaillé au fil des années.',
        items: [
          {
            title: 'Job Finder Bot & Scraper',
            description: 'Solution complète de recherche d\'emploi avec scraping web et intégration bot Telegram. Fonctionnalités : résumé d\'offres d\'emploi par IA (Mistral AI), stockage MongoDB, et livraison automatisée aux utilisateurs.',
            link: 'https://github.com/ClaudelMbz/jobFinder',
            tags: ['Python', 'Bot Telegram', 'Web Scraping', 'IA', 'MongoDB']
          },
          {
            title: 'PromptForge',
            description: 'Extension de navigateur qui optimise les interactions avec les modèles de langage. Algorithmes d\'optimisation de prompts (Primer & Mastermind), intégration avec ChatGPT, Gemini, et DeepSeek.',
            link: 'https://github.com/ClaudelMbz/PromptForge-SPEA-',
            tags: ['JavaScript', 'Extension Chrome', 'IA', 'LLM', 'Extension Navigateur']
          },
          {
            title: 'Système de Scraping d\'Emplois',
            description: 'Système avancé de scraping web pour offres d\'emploi avec intégration IA. Automatise la découverte, le traitement et le stockage avec extraction intelligente de données.',
            link: 'https://github.com/ClaudelMbz/jobScraping',
            tags: ['Python', 'Web Scraping', 'Traitement de Données', 'Automatisation', 'IA']
          }
        ]
      },
      certifications: {
        title: 'Certifications',
        items: [
          {
            name: 'CS50x - Introduction à l\'Informatique',
            institution: 'Université Harvard',
            date: 'Décembre 2023',
            link: null,
            image: '/CS50x.png',
            download: false
          },
          {
            name: 'CS50 Introduction à l\'Intelligence Artificielle avec Python',
            institution: 'Université Harvard',
            date: 'Mars 2024',
            link: null,
            image: '/CS50AI.png',
            download: false
          },
          {
            name: 'AWS BNB Node Runners',
            institution: 'Amazon Web Services',
            date: 'Janvier 2024',
            link: null,
            image: '/awsbnbrunners.jpg',
            download: false
          }
        ]
      }
    }
  };

  const t = content[language];

  useEffect(() => {
    const handleScroll = () => {
      const sections = ['bio', 'experience', 'projects'];
      const scrollPosition = window.scrollY + 100;

      for (const section of sections) {
        const element = document.getElementById(section);
        if (element) {
          const { offsetTop, offsetHeight } = element;
          if (scrollPosition >= offsetTop && scrollPosition < offsetTop + offsetHeight) {
            setActiveSection(section);
            break;
          }
        }
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
      setIsMenuOpen(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-emerald-900 to-gray-900 text-white">
      {/* Navigation */}
      <nav className="fixed top-0 left-0 right-0 z-50 bg-gray-900/80 backdrop-blur-lg border-b border-emerald-500/20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="text-xl font-bold text-emerald-400">Claudel Mubenzem</div>
            
            {/* Desktop Navigation */}
            <div className="hidden md:flex items-center space-x-8">
              {Object.entries(t.nav).map(([key, value]) => (
                <button
                  key={key}
                  onClick={() => scrollToSection(key)}
                  className={`text-sm font-medium transition-colors hover:text-emerald-400 ${
                    activeSection === key ? 'text-emerald-400' : 'text-gray-300'
                  }`}
                >
                  {value}
                </button>
              ))}
              <button
                onClick={() => setLanguage(language === 'en' ? 'fr' : 'en')}
                className="px-3 py-1 text-sm font-medium bg-emerald-600 hover:bg-emerald-700 rounded-lg transition-colors"
              >
                {language === 'en' ? 'FR' : 'EN'}
              </button>
            </div>

            {/* Mobile Menu Button */}
            <button
              onClick={() => setIsMenuOpen(!isMenuOpen)}
              className="md:hidden p-2 rounded-lg hover:bg-gray-800 transition-colors"
            >
              {isMenuOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          </div>
        </div>

        {/* Mobile Menu */}
        {isMenuOpen && (
          <div className="md:hidden bg-gray-900 border-t border-emerald-500/20">
            <div className="px-4 py-4 space-y-3">
              {Object.entries(t.nav).map(([key, value]) => (
                <button
                  key={key}
                  onClick={() => scrollToSection(key)}
                  className="block w-full text-left px-4 py-2 rounded-lg hover:bg-gray-800 transition-colors"
                >
                  {value}
                </button>
              ))}
              <button
                onClick={() => setLanguage(language === 'en' ? 'fr' : 'en')}
                className="block w-full text-left px-4 py-2 bg-emerald-600 hover:bg-emerald-700 rounded-lg transition-colors"
              >
                {language === 'en' ? 'Français' : 'English'}
              </button>
            </div>
          </div>
        )}
      </nav>

      {/* Hero Section */}
      <section id="bio" className="pt-32 pb-20 px-4 relative overflow-hidden">
        <div className="absolute inset-0 opacity-10">
          <div className="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxkZWZzPjxwYXR0ZXJuIGlkPSJncmlkIiB3aWR0aD0iNDAiIGhlaWdodD0iNDAiIHBhdHRlcm5Vbml0cz0idXNlclNwYWNlT25Vc2UiPjxwYXRoIGQ9Ik0gNDAgMCBMIDAgMCAwIDQwIiBmaWxsPSJub25lIiBzdHJva2U9IiMxMGIzODEiIHN0cm9rZS13aWR0aD0iMSIvPjwvcGF0dGVybj48L2RlZnM+PHJlY3Qgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSIgZmlsbD0idXJsKCNncmlkKSIvPjwvc3ZnPg==')]"></div>
        </div>
        
        <div className="max-w-6xl mx-auto relative z-10">
          <div className="grid md:grid-cols-2 gap-12 items-center">
            {/* Left side - Photo and personal info */}
            <div className="text-center md:text-left">
              <div className="w-64 h-64 mx-auto md:mx-0 mb-8 rounded-full bg-gradient-to-br from-emerald-400 to-emerald-600 p-1">
                <div className="w-full h-full rounded-full overflow-hidden">
                  <img 
                    src={avatarImg} 
                    alt="Claudel Mubenzem" 
                    className="w-full h-full object-cover"
                  />
                </div>
              </div>
              
              <h1 className="text-4xl md:text-5xl font-bold mb-4 bg-gradient-to-r from-emerald-400 to-cyan-400 bg-clip-text text-transparent">
                {t.hero.name}
              </h1>
              
              <p className="text-xl md:text-2xl text-gray-300 mb-4">
                {t.hero.title}
              </p>
              
              <p className="text-lg text-emerald-400 mb-8">
                {t.hero.status}
              </p>

              <div className="flex flex-wrap justify-center md:justify-start gap-4">
                <a
                  href="https://linkedin.com"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="px-6 py-3 bg-emerald-600 hover:bg-emerald-700 rounded-lg font-medium transition-all hover:scale-105 flex items-center gap-2"
                >
                  <Linkedin size={20} />
                  LinkedIn
                </a>
                <button className="px-6 py-3 bg-gray-800 hover:bg-gray-700 rounded-lg font-medium transition-all hover:scale-105 flex items-center gap-2">
                  <Download size={20} />
                  {t.hero.downloadCV}
                </button>
                <a
                  href="https://github.com"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="px-6 py-3 bg-gray-800 hover:bg-gray-700 rounded-lg font-medium transition-all hover:scale-105 flex items-center gap-2"
                >
                  <Github size={20} />
                  GitHub
                </a>
              </div>
            </div>

            {/* Right side - About section */}
            <div className="bg-gray-800/50 backdrop-blur-sm rounded-2xl p-8">
              <h2 className="text-3xl font-bold mb-6 text-emerald-400">{t.about.title}</h2>
              <p className="text-lg text-gray-300 leading-relaxed whitespace-pre-line">
                {t.about.description}
              </p>
            </div>
          </div>

          {/* Interests */}
          <div className="mt-16 text-left bg-gray-800/50 backdrop-blur-sm rounded-2xl p-8">
            <h3 className="text-2xl font-bold mb-6 text-emerald-400">{t.interests.title}</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {t.interests.items.map((interest, index) => (
                <div key={index} className="flex items-start gap-3">
                  <ChevronRight className="text-emerald-400 flex-shrink-0 mt-1" size={20} />
                  <span className="text-gray-300">{interest}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* Experience & Education Section */}
      <section id="experience" className="py-20 px-4 bg-gray-900/50">
        <div className="max-w-6xl mx-auto">
          {/* Experience */}
          <div className="mb-16">
            <h2 className="text-4xl font-bold mb-8 text-emerald-400">{t.experience.title}</h2>
            <div className="relative">
              {/* Timeline line */}
              <div className="absolute left-6 top-0 bottom-0 w-0.5 bg-gradient-to-b from-emerald-500 to-emerald-300"></div>
              
              <div className="space-y-8">
                {t.experience.jobs.map((job, index) => (
                  <div key={index} className="relative flex items-start">
                    {/* Timeline dot */}
                    <div className="absolute left-4 w-4 h-4 bg-emerald-500 rounded-full border-4 border-gray-900 z-10"></div>
                    
                    {/* Content card */}
                    <div className="ml-12 bg-gray-800/50 backdrop-blur-sm rounded-xl p-6 border border-emerald-500/20 hover:border-emerald-500/40 transition-colors flex-1">
                      <h3 className="text-xl font-bold text-white mb-2">{job.role}</h3>
                      <p className="text-emerald-400 font-medium mb-2">{job.company}</p>
                      <p className="text-sm text-gray-400 mb-3">{job.period}</p>
                      <p className="text-gray-300">{job.description}</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Education - Connected Timeline */}
          <div>
            <h2 className="text-4xl font-bold mb-8 text-emerald-400">{t.education.title}</h2>
            <div className="relative">
              {/* Timeline line continuation */}
              <div className="absolute left-6 top-0 bottom-0 w-0.5 bg-gradient-to-b from-emerald-300 to-emerald-200"></div>
              
              <div className="space-y-8">
                {t.education.items.map((edu, index) => (
                  <div key={index} className="relative flex items-start">
                    {/* Timeline dot */}
                    <div className="absolute left-4 w-4 h-4 bg-emerald-400 rounded-full border-4 border-gray-900 z-10"></div>
                    
                    {/* Content card */}
                    <div className="ml-12 bg-gray-800/50 backdrop-blur-sm rounded-xl p-6 border border-emerald-500/20 hover:border-emerald-500/40 transition-colors flex-1">
                    <h3 className="text-xl font-bold text-white mb-2">{edu.degree}</h3>
                    <p className="text-emerald-400 font-medium mb-2">{edu.institution}</p>
                    <p className="text-sm text-gray-400 mb-3">{edu.period}</p>
                    {edu.specialization && (
                      <p className="text-gray-300 mb-3">{edu.specialization}</p>
                    )}
                    {edu.courses && (
                      <div className="mt-3">
                        <p className="text-sm text-emerald-400 font-medium mb-2">Key Courses:</p>
                        <div className="flex flex-wrap gap-2">
                          {edu.courses.map((course, courseIndex) => (
                            <span
                              key={courseIndex}
                              className="px-2 py-1 bg-emerald-600/20 text-emerald-300 rounded text-xs"
                            >
                              {course}
                            </span>
                          ))}
                        </div>
                      </div>
                    )}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Skills Section */}
      <section className="py-20 px-4 bg-gray-800/30">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl font-bold mb-8 text-emerald-400">{t.skills.title}</h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {t.skills.items.map((skill, index) => (
              <div key={index} className="bg-gray-800/50 backdrop-blur-sm rounded-xl p-6 border border-emerald-500/20 hover:border-emerald-500/40 transition-all hover:scale-105">
                <h3 className="text-lg font-bold text-white mb-2">{skill.name}</h3>
                <p className="text-sm text-gray-400 mb-3">{skill.desc}</p>
                <div className="w-full bg-gray-700 rounded-full h-2">
                  <div
                    className="bg-gradient-to-r from-emerald-500 to-cyan-500 h-2 rounded-full transition-all duration-1000"
                    style={{ width: `${skill.level}%` }}
                  ></div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Certifications Section */}
      <section className="py-20 px-4 bg-gray-900/50">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl font-bold mb-8 text-emerald-400 text-center">{t.certifications.title}</h2>
          <div className="grid md:grid-cols-3 gap-8">
            {t.certifications.items.map((cert, index) => (
              <div key={index} className="bg-gray-800/50 backdrop-blur-sm rounded-xl p-6 border border-emerald-500/20 hover:border-emerald-500/40 transition-all hover:scale-105">
                {cert.image && (
                  <div className="mb-4">
                    <img 
                      src={cert.image} 
                      alt={cert.name}
                      className="w-full h-48 object-contain rounded-lg bg-gray-700/30 p-2"
                    />
                  </div>
                )}
                <h3 className="text-lg font-bold text-white mb-2">{cert.name}</h3>
                <p className="text-emerald-400 font-medium mb-2">{cert.institution}</p>
                <p className="text-sm text-gray-400">{cert.date}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Projects Section */}
      <section id="projects" className="py-20 px-4">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-12">
            <h2 className="text-4xl font-bold mb-4 text-emerald-400">{t.projects.title}</h2>
            <p className="text-xl text-gray-300">{t.projects.subtitle}</p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {t.projects.items.map((project, index) => (
              <div key={index} className="bg-gray-800/50 backdrop-blur-sm rounded-xl p-6 border border-emerald-500/20 hover:border-emerald-500/40 transition-all hover:scale-105 group">
                <h3 className="text-2xl font-bold text-white mb-3 group-hover:text-emerald-400 transition-colors">
                  {project.title}
                </h3>
                <p className="text-gray-300 mb-4">{project.description}</p>
                <div className="flex flex-wrap gap-2 mb-4">
                  {project.tags.map((tag, tagIndex) => (
                    <span
                      key={tagIndex}
                      className="px-3 py-1 bg-emerald-600/20 text-emerald-400 rounded-full text-sm"
                    >
                      {tag}
                    </span>
                  ))}
                </div>
                <a
                  href={project.link}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-2 text-emerald-400 hover:text-emerald-300 transition-colors"
                >
                  View Project <ExternalLink size={16} />
                </a>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 border-t border-emerald-500/20 py-12 px-4">
        <div className="max-w-6xl mx-auto text-center">
          <div className="flex justify-center gap-6 mb-6">
            <a href="https://github.com" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-emerald-400 transition-colors">
              <Github size={24} />
            </a>
            <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-emerald-400 transition-colors">
              <Linkedin size={24} />
            </a>
            <a href="mailto:contact@example.com" className="text-gray-400 hover:text-emerald-400 transition-colors">
              <Mail size={24} />
            </a>
          </div>
          <p className="text-gray-400 mb-2">
            © 2025 Claudel Mubenzem. This work is licensed under CC BY NC ND 4.0
          </p>
          <p className="text-gray-500 text-sm">
            Made with React, Tailwind CSS & ❤️
          </p>
        </div>
      </footer>
    </div>
  );
};

export default Portfolio;
