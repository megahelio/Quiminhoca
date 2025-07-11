// App.tsx - Componente principal
import { useState } from 'react';
import axios from 'axios';
import { Input, Button, Card, CardContent, CardHeader } from '@mui/material';

function App() {
  const [notation, setNotation] = useState('');
  const [type, setType] = useState('smiles');
  const [data, setData] = useState<any | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const res = await axios.post('http://localhost:8000/api/parse', {
      notation,
      type,
    });
    setData(res.data);
  };

  return (
    <div className="min-h-screen bg-gray-100 p-4 grid grid-cols-1 md:grid-cols-2 gap-4">
      <form onSubmit={handleSubmit} className="space-y-4">
        <Input
          placeholder="Introduce la notación química (ej: C6H6)"
          value={notation}
          onChange={(e) => setNotation(e.target.value)}
        />
        <select
          value={type}
          onChange={(e) => setType(e.target.value)}
          className="border p-2 rounded-md"
        >
          <option value="formula" selected>Fórmula</option>
          <option disabled value="smiles">SMILES</option>
          <option disabled value="inchi">InChI</option>
        </select>
        <Button type="submit">Consultar</Button>
      </form>

      {data && (
        <Card>
          <CardHeader>
            <h2 className="text-xl font-semibold">{data.name}</h2>
            <span className="text-gray-600">{data.formula}</span>
          </CardHeader>
          <CardContent className="space-y-2">
            <p>Masa molar: {data.molar_mass} g/mol</p>
          </CardContent>
        </Card>
      )}
    </div>
  );
}

export default App;