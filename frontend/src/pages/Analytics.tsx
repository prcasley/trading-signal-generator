import React from 'react';

export const Analytics: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
          Analytics
        </h1>
        <p className="mt-2 text-gray-600 dark:text-gray-400">
          Detailed performance analytics and insights
        </p>
      </div>

      <div className="bg-white dark:bg-dark-800 rounded-lg border border-gray-200 dark:border-dark-700 p-6">
        <h2 className="text-lg font-medium text-gray-900 dark:text-white mb-4">
          Coming Soon
        </h2>
        <p className="text-gray-600 dark:text-gray-400">
          Advanced analytics and performance tracking features will be available here.
        </p>
      </div>
    </div>
  );
};