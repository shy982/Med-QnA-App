import React, {useState} from 'react';

const FileUploader = ({onFileUpload}) => {
    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileChange = (e) => {
        const file = e.target.files[0];
        setSelectedFile(file);
        handleUpload();
    };

    const handleUpload = () => {
        if (!selectedFile) {
            alert('Please select a text file to upload.');
            return;
        }

        const reader = new FileReader();

        reader.onload = (event) => {
            const fileContent = event.target.result;
            console.log(fileContent)
            onFileUpload(fileContent);
        };

        reader.readAsText(selectedFile);
    };

    return (
        <div className="flex items-center">
            <label htmlFor="file-input"
                   className="cursor-pointer bg-blue-500 text-white px-1 py-2 rounded-md mr-2 hover:bg-blue-600">
                <img width="20" height="20"
                     src="https://img.icons8.com/external-filled-agus-raharjo/64/external-paper-clip-glyph-website-ui-filled-agus-raharjo.png"
                     alt="external-paper-clip-glyph-website-ui-filled-agus-raharjo"/>
            </label>
            <input
                type="file"
                accept=".txt"
                onChange={handleFileChange}
                className="hidden"
                id="file-input"
            />
        </div>
    );
};

export default FileUploader;
