import React from 'react';

export const Settings: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
          Settings
        </h1>
        <p className="mt-2 text-gray-600 dark:text-gray-400">
          Configure your trading preferences and API settings
        </p>
      </div>

      <div className="bg-white dark:bg-dark-800 rounded-lg border border-gray-200 dark:border-dark-700 p-6">
        <h2 className="text-lg font-medium text-gray-900 dark:text-white mb-4">
          API Configuration
        </h2>
        <p className="text-gray-600 dark:text-gray-400">
          API settings and configuration options will be available here.
        </p>
      </div>
    </div>
  );
};