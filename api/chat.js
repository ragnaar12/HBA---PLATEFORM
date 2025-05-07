const fetch = require('node-fetch');  // Si tu n'as pas cette dépendance, tu peux l'installer via npm

module.exports = async (req, res) => {
  if (req.method === 'POST') {
    const { message } = req.body;
    
    // Utiliser la variable d'environnement COHERE_API_KEY pour sécuriser la clé API
    const API_KEY = process.env.COHERE_API_KEY;  // Utilisation de la clé stockée dans les variables d'environnement
    const API_URL = "https://api.cohere.ai/v1/chat";

    try {
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${API_KEY}`,
        },
        body: JSON.stringify({
          model: "large",  // Remplace par le modèle que tu utilises
          messages: [{ role: "user", content: message }],
          temperature: 0.7,
          max_tokens: 1000,
        })
      });

      // Afficher la réponse brute pour déboguer
      const responseText = await response.text();
      console.log('Réponse brute:', responseText);  // Cette ligne te permettra de voir la réponse exacte

      // Convertir la réponse en JSON
      let data;
      try {
        data = JSON.parse(responseText);
      } catch (e) {
        console.error('Erreur lors du parsing JSON:', e);
        return res.status(500).json({ error: 'Réponse de l\'API non valide' });
      }

      if (data?.choices?.[0]?.message?.content) {
        res.status(200).json({ reply: data.choices[0].message.content });
      } else {
        res.status(400).json({ error: 'Réponse inattendue de l\'API Cohere.' });
      }
    } catch (error) {
      res.status(500).json({ error: error.message });
    }
  } else {
    res.status(405).json({ error: 'Méthode non autorisée' });
  }
};












