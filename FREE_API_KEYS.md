# Free API Keys Setup Guide

This project supports multiple FREE AI providers with high rate limits. You only need ONE of these keys to get started!

## 🚀 Recommended: Groq (Fastest & Highest Free Limit)

**Why Groq?** 14,400 requests/day, super fast inference

1. Go to: https://console.groq.com/keys
2. Sign up with GitHub/Google
3. Click "Create API Key"
4. Copy the key and add to `.env`:
   ```
   GROQ_API_KEY=gsk_your_key_here
   ```

## Alternative Free Providers

### OpenRouter (Free Tier)
1. Go to: https://openrouter.ai/keys
2. Sign up
3. Get API key
4. Add to `.env`:
   ```
   OPENROUTER_API_KEY=sk-or-v1-your_key_here
   ```

### Together AI ($25 Free Credit)
1. Go to: https://api.together.xyz/settings/api-keys
2. Sign up
3. Get $25 free credit
4. Add to `.env`:
   ```
   TOGETHER_API_KEY=your_key_here
   ```

### Google Gemini (Backup)
1. Go to: https://aistudio.google.com/apikey
2. Create new project
3. Generate API key
4. Add to `.env`:
   ```
   GOOGLE_API_KEY=AIzaSy...
   ```

## Provider Priority

The system tries providers in this order (configurable in `.env`):
1. **Groq** (default - fastest)
2. OpenRouter
3. Together AI  
4. Google Gemini

Change priority by setting:
```
PRIMARY_PROVIDER=groq
```

## Rate Limits Comparison

| Provider | Free Tier | Speed | Models |
|----------|-----------|-------|--------|
| **Groq** | 14,400 req/day | ⚡⚡⚡ | Llama 3.3 70B |
| OpenRouter | Limited free | ⚡⚡ | Various |
| Together AI | $25 credit | ⚡⚡ | Llama 3.1 8B |
| Google | 1,500 req/day | ⚡ | Gemini 2.0 |

## Quick Start

1. Get a Groq API key (takes 2 minutes)
2. Add it to `.env`
3. Run: `streamlit run streamlit_app.py`
4. Start researching! 🎉
