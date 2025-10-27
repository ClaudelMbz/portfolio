# Claudel Mubenzem - Portfolio

A modern, responsive portfolio website built with React and Tailwind CSS, showcasing my work as an aspiring AI & Automation Engineer.

## Features

- 🌐 **Bilingual Support**: English and French language toggle
- 📱 **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- 🎨 **Modern UI**: Beautiful gradient backgrounds and glass-morphism effects
- ⚡ **Fast Performance**: Built with Vite for lightning-fast development and builds
- 🎯 **Smooth Navigation**: Auto-scrolling navigation with active section highlighting
- 📊 **Interactive Elements**: Animated skill bars and hover effects

## Sections

- **Bio**: Personal introduction and professional summary
- **Experience**: Work history and internships
- **Education**: Academic background and qualifications
- **Skills**: Technical expertise with proficiency levels
- **Projects**: Selected work and contributions
- **Certifications**: Professional certifications and achievements
- **Languages**: Language proficiency levels

## Tech Stack

- **React 18**: Modern React with hooks
- **Tailwind CSS**: Utility-first CSS framework
- **Lucide React**: Beautiful, customizable icons
- **Vite**: Fast build tool and development server

## Getting Started

### Prerequisites

- Node.js (version 16 or higher)
- npm or yarn

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd claudel-portfolio
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open your browser and navigate to `http://localhost:3000`

### Build for Production

```bash
npm run build
```

The built files will be in the `dist` directory.

### Preview Production Build

```bash
npm run preview
```

## Customization

### Personal Information

Edit the `content` object in `src/Portfolio.jsx` to update:
- Personal details and bio
- Work experience and education
- Skills and proficiency levels
- Project descriptions and links
- Contact information

### Styling

The project uses Tailwind CSS with custom configurations in `tailwind.config.js`. You can:
- Modify color schemes in the theme configuration
- Add custom animations and transitions
- Update typography and spacing

### Adding New Sections

1. Add the section to the `nav` object in both language versions
2. Create the section JSX in the main component
3. Update the scroll detection logic in the `useEffect` hook

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

- **Email**: contact@claudelmubenzem.dev
- **LinkedIn**: [linkedin.com/in/claudelmubenzem](https://linkedin.com/in/claudelmubenzem)
- **GitHub**: [github.com/claudelmubenzem](https://github.com/claudelmubenzem)

---

Made with ❤️ by Claudel Mubenzem