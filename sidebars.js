/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */

// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  tutorialSidebar: [
    'index',
    'quickstart',
    {
      type: 'category',
      label: 'Modules',
      items: [
        'modules/module1-ros2/ros2-fundamentals',
        'modules/module1-ros2/ros2-navigation',
        'modules/module1-ros2/multi-robot-systems',
        'modules/module2-simulation/gazebo-simulation',
        'modules/module2-simulation/unity-visualization',
        'modules/module3-isaac/isaac-sim-basics',
        'modules/module3-isaac/synthetic-data-generation',
        'modules/module4-vla/vla-introduction',
        'modules/module4-vla/vla-implementation',
        'modules/module4-vla/vla-deployment',
      ],
    },
    {
      type: 'category',
      label: 'Capstone Project',
      items: [
        'capstone/capstone-project',
      ],
    },
    {
      type: 'category',
      label: 'Lab Infrastructure',
      items: [
        'infrastructure/lab-tiers-overview',
        'infrastructure/proxy-tier',
        'infrastructure/miniature-tier',
        'infrastructure/premium-tier',
        'infrastructure/deployment-options',
      ],
    },
    {
      type: 'category',
      label: 'Appendices',
      items: [
        'appendices/glossary',
        'appendices/week-by-week',
        'appendices/roi-analysis',
        'appendices/references',
      ],
    },
  ],
};

module.exports = sidebars;
