<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="720" viewBox="0 0 1200 720">
  <style>
    .box { fill: #f7f9fc; stroke: #355070; stroke-width: 2; rx: 18; ry: 18; }
    .data { fill: #eef6ff; stroke: #457b9d; stroke-width: 2; rx: 18; ry: 18; }
    .title { font: 700 28px Arial, sans-serif; fill: #1f2937; }
    .label { font: 600 18px Arial, sans-serif; fill: #1f2937; }
    .small { font: 400 14px Arial, sans-serif; fill: #374151; }
    .arrow { stroke: #4b5563; stroke-width: 2.5; fill: none; marker-end: url(#arrow); }
  </style>
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#4b5563"/>
    </marker>
  </defs>

  <text x="40" y="45" class="title">RAG E-commerce Gift Recommendation System</text>

  <rect x="40" y="95" width="250" height="90" class="box"/>
  <text x="70" y="135" class="label">Streamlit Demo UI</text>
  <text x="70" y="160" class="small">Shopper selects gifter, recipient,</text>
  <text x="70" y="180" class="small">occasion, budget, and top-k ideas</text>

  <rect x="350" y="95" width="270" height="90" class="box"/>
  <text x="382" y="135" class="label">GiftRecommendationService</text>
  <text x="382" y="160" class="small">Coordinates retrieval, reranking,</text>
  <text x="382" y="180" class="small">and explanation generation</text>

  <rect x="690" y="95" width="270" height="90" class="box"/>
  <text x="725" y="135" class="label">Retriever</text>
  <text x="725" y="160" class="small">Builds contextual query from</text>
  <text x="725" y="180" class="small">recipient profile + gift scenario</text>

  <rect x="690" y="250" width="270" height="100" class="box"/>
  <text x="730" y="292" class="label">Embedding Provider</text>
  <text x="730" y="317" class="small">Sentence Transformers</text>
  <text x="730" y="337" class="small">with TF-IDF fallback</text>

  <rect x="690" y="415" width="270" height="100" class="box"/>
  <text x="735" y="457" class="label">Vector Search</text>
  <text x="735" y="482" class="small">Semantic similarity over</text>
  <text x="735" y="502" class="small">product catalog text</text>

  <rect x="1010" y="250" width="150" height="100" class="box"/>
  <text x="1045" y="292" class="label">Reranker</text>
  <text x="1032" y="317" class="small">Style + budget +</text>
  <text x="1038" y="337" class="small">occasion + social</text>

  <rect x="1010" y="415" width="150" height="100" class="box"/>
  <text x="1028" y="457" class="label">Generator</text>
  <text x="1033" y="482" class="small">LLM optional,</text>
  <text x="1028" y="502" class="small">rule-based fallback</text>

  <rect x="350" y="580" width="420" height="90" class="box"/>
  <text x="395" y="620" class="label">Explainable Recommendations</text>
  <text x="395" y="645" class="small">Top summary + recommendation cards + retrieved product table</text>

  <rect x="40" y="280" width="250" height="90" class="data"/>
  <text x="80" y="320" class="label">products.csv</text>
  <text x="80" y="345" class="small">Catalog metadata, styles,</text>
  <text x="80" y="365" class="small">prices, descriptions</text>

  <rect x="40" y="405" width="250" height="90" class="data"/>
  <text x="80" y="445" class="label">users.json</text>
  <text x="80" y="470" class="small">Recipient preferences, browsing,</text>
  <text x="80" y="490" class="small">purchase history</text>

  <rect x="40" y="530" width="250" height="90" class="data"/>
  <text x="80" y="570" class="label">social_graph.json</text>
  <text x="80" y="595" class="small">Closeness and interaction</text>
  <text x="80" y="615" class="small">signals between users</text>

  <path d="M290 140 L350 140" class="arrow"/>
  <path d="M620 140 L690 140" class="arrow"/>
  <path d="M825 185 L825 250" class="arrow"/>
  <path d="M825 350 L825 415" class="arrow"/>
  <path d="M960 300 L1010 300" class="arrow"/>
  <path d="M1085 350 L1085 415" class="arrow"/>
  <path d="M1010 465 L770 625" class="arrow"/>
  <path d="M560 185 L560 580" class="arrow"/>
  <path d="M290 325 L690 455" class="arrow"/>
  <path d="M290 450 L690 140" class="arrow"/>
  <path d="M290 575 L1010 300" class="arrow"/>
</svg>
