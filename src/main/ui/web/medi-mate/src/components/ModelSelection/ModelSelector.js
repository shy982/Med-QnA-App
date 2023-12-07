// ModelSelector.js

import React from 'react';

const ModelSelector = ({ onModelChange, handleReset }) => {
  const models = ['Debug', 'Open AI', 'RAG + Open AI', 'RAG + LLAMA'];

  return (
    <select onChange={(e) => {onModelChange(e.target.value); handleReset();} } className="text-sm sm:text-base text-neutral-900 font-semibold rounded-lg px-4 py-2 bg-neutral-200 hover:bg-neutral-300 focus:outline-none focus:ring-1 focus:ring-neutral-300">
      {models.map(model => (
        <option key={model} value={model}>{model}</option>
      ))}
    </select>
  );
};

export default ModelSelector;
