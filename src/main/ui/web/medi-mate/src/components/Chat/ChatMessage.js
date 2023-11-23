import React from 'react';
// import PropTypes from 'prop-types'; // Uncomment if you want to use PropTypes

const ChatMessage = ({ message }) => {
  return (
    <div className={`flex flex-col ${message.role === "assistant" ? "items-start" : "items-end"}`}>
      <div
        className={`flex items-center ${message.role === "assistant" ? "bg-neutral-200 text-neutral-900" : "bg-blue-500 text-white"} rounded-2xl px-3 py-2 max-w-[67%] whitespace-pre-wrap`}
        style={{ overflowWrap: "anywhere" }}
      >
        {message.content}
      </div>
    </div>
  );
};

// If using PropTypes
// ChatMessage.propTypes = {
//   message: PropTypes.shape({
//     role: PropTypes.oneOf(["assistant", "user"]).isRequired,
//     content: PropTypes.string.isRequired,
//   }).isRequired,
// };

export default ChatMessage;
