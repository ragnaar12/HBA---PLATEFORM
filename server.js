import express from 'express';
import dotenv from 'dotenv';
import fetch from 'node-fetch';
import path from 'path';
import { fileURLToPath } from 'url';

dotenv.config();
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());
app.use(express.static('public'));

app.post('/chat', async (req, res) => {
  const { message } = req.body;
  try {
    const response = await fetch('https://api.cohere.ai/v1/chat', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${process.env.COHERE_API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        model: 'command-r-plus',
        message,
        chat_history: [],
        temperature: 0.9
      })
    });

    const data = await response.json();
    res.json({ reply: data.text || "Je n'ai pas compris." });
  } catch (error) {
    res.status(500).json({ error: 'Erreur serveur' });
  }
});

app.listen(port, () => console.log(`UniChat écoute sur http://localhost:${port}`));














