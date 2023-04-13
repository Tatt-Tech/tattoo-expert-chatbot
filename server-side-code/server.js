const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.post('/api/chat', (req, res) => {
  // Your chatbot API logic goes here
  // For example:
  const userMessage = req.body.message;
  const chatbotResponse = 'This is a sample response to: ' + userMessage;
  res.json({ answer: chatbotResponse });
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
