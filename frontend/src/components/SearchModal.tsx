import React, { useState, useEffect } from 'react';
import { Dialog } from '@headlessui/react';
import { MagnifyingGlassIcon, XMarkIcon } from '@heroicons/react/24/outline';

interface SearchModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export const SearchModal: React.FC<SearchModalProps> = ({ isOpen, onClose }) => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([
    { symbol: 'AAPL', name: 'Apple Inc.', price: '$150.25', change: '+1.2%' },
    { symbol: 'GOOGL', name: 'Alphabet Inc.', price: '$2800.50', change: '-0.5%' },
    { symbol: 'MSFT', name: 'Microsoft Corporation', price: '$280.75', change: '+0.8%' },
    { symbol: 'TSLA', name: 'Tesla, Inc.', price: '$220.30', change: '+2.1%' },
  ]);

  useEffect(() => {
    if (isOpen) {
      setQuery('');
    }
  }, [isOpen]);

  return (
    <Dialog open={isOpen} onClose={onClose} className="relative z-50">
      <div className="fixed inset-0 bg-black/30 backdrop-blur-sm" aria-hidden="true" />
      
      <div className="fixed inset-0 flex items-start justify-center pt-16">
        <Dialog.Panel className="mx-auto max-w-2xl w-full bg-white dark:bg-dark-800 rounded-xl shadow-strong border border-gray-200 dark:border-dark-600">
          {/* Search Input */}
          <div className="flex items-center border-b border-gray-200 dark:border-dark-600 px-4">
            <MagnifyingGlassIcon className="h-5 w-5 text-gray-400 dark:text-gray-500" />
            <input
              type="text"
              placeholder="Search stocks, symbols, or companies..."
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              className="w-full bg-transparent border-none py-4 pl-4 pr-4 text-gray-900 dark:text-white placeholder-gray-500 dark:placeholder-gray-400 focus:outline-none"
              autoFocus
            />
            <button
              onClick={onClose}
              className="p-1 text-gray-400 dark:text-gray-500 hover:text-gray-500 dark:hover:text-gray-400"
            >
              <XMarkIcon className="h-5 w-5" />
            </button>
          </div>

          {/* Results */}
          <div className="max-h-96 overflow-y-auto p-4">
            {query ? (
              <div className="space-y-2">
                {results
                  .filter(stock => 
                    stock.symbol.toLowerCase().includes(query.toLowerCase()) ||
                    stock.name.toLowerCase().includes(query.toLowerCase())
                  )
                  .map((stock) => (
                    <div
                      key={stock.symbol}
                      className="flex items-center justify-between p-3 rounded-lg hover:bg-gray-50 dark:hover:bg-dark-700 cursor-pointer transition-colors duration-200"
                      onClick={() => {
                        console.log('Selected:', stock.symbol);
                        onClose();
                      }}
                    >
                      <div>
                        <div className="font-medium text-gray-900 dark:text-white">
                          {stock.symbol}
                        </div>
                        <div className="text-sm text-gray-500 dark:text-gray-400">
                          {stock.name}
                        </div>
                      </div>
                      <div className="text-right">
                        <div className="font-medium text-gray-900 dark:text-white">
                          {stock.price}
                        </div>
                        <div className={`text-sm ${
                          stock.change.startsWith('+') ? 'text-green-600' : 'text-red-600'
                        }`}>
                          {stock.change}
                        </div>
                      </div>
                    </div>
                  ))}
              </div>
            ) : (
              <div className="text-center py-8">
                <MagnifyingGlassIcon className="mx-auto h-12 w-12 text-gray-400 dark:text-gray-500" />
                <h3 className="mt-4 text-sm font-medium text-gray-900 dark:text-white">
                  Search for stocks
                </h3>
                <p className="mt-2 text-sm text-gray-500 dark:text-gray-400">
                  Enter a symbol or company name to get started
                </p>
              </div>
            )}
          </div>
        </Dialog.Panel>
      </div>
    </Dialog>
  );
};