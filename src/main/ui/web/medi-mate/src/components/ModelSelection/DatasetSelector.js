import React, { useEffect, useState } from "react";

const DatasetSelector = ({ isRAGEnabled, onDatasetChange, handleReset }) => {
  const datasets = ["NFCorpus", "PubMedQA", "CORD19"];
  const [selectedDataset, setSelectedDataset] = useState("nfcorpus");

  useEffect(() => {
    if (!isRAGEnabled) {
      setSelectedDataset("nfcorpus");
      onDatasetChange("nfcorpus");
    }
  }, [isRAGEnabled, onDatasetChange]);

  const handleChange = (e) => {
    setSelectedDataset(e.target.value);
    onDatasetChange(e.target.value);
    handleReset();
  };

  return (
    <select
      value={selectedDataset}
      disabled={!isRAGEnabled}
      onChange={handleChange}
      className="text-sm sm:text-base text-neutral-900 font-semibold rounded-lg px-4 py-2 bg-neutral-200 hover:bg-neutral-300 focus:outline-none focus:ring-1 focus:ring-neutral-300"
    >
      {datasets.map((dataset) => (
        <option key={dataset} value={dataset}>
          {dataset}
        </option>
      ))}
    </select>
  );
};

export default DatasetSelector;
