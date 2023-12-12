import React, { useEffect, useRef, useState } from "react";
import { MdMic, MdStop } from "react-icons/md";

const MicButton = ({
  onTranscription,
  updatePlaceholder,
  messageSent,
  setMessageSent,
}) => {
  const [isListening, setIsListening] = useState(false);
  const recognitionRef = useRef(null);

  const startListening = () => {
    if ("webkitSpeechRecognition" in window) {
      const SpeechRecognition =
        window.webkitSpeechRecognition || window.SpeechRecognition;
      recognitionRef.current = new SpeechRecognition();
      recognitionRef.current.continuous = true;
      recognitionRef.current.interimResults = true;

      recognitionRef.current.onresult = (event) => {
        const transcript = Array.from(event.results)
          .map((result) => result[0])
          .map((result) => result.transcript)
          .join("");
        onTranscription(transcript);
      };

      recognitionRef.current.start();
      setIsListening(true);
      updatePlaceholder(true);
    } else {
      alert("Speech recognition not supported in this browser.");
    }
  };

  const stopListening = () => {
    if (recognitionRef.current) {
      recognitionRef.current.stop();
      setIsListening(false);
      updatePlaceholder(false);
    }
  };
  useEffect(() => {
    if (messageSent) {
      stopListening();
      setMessageSent(false);
    }
  });
  const toggleListening = () => {
    if (isListening) {
      stopListening();
    } else {
      startListening();
    }
  };

  return (
    <button
      onClick={toggleListening}
      className={`absolute right-11 bottom-1.5 h-8 w-8 hover:cursor-pointer rounded-full p-1 ${
        isListening ? "bg-red-500 animate-pulse" : "bg-green-500"
      } text-white hover:opacity-80 flex items-center justify-center`}
    >
      {isListening ? <MdStop size="1.2em" /> : <MdMic size="1.2em" />}
    </button>
  );
};

export default MicButton;
