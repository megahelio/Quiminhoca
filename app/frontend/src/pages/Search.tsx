// App.tsx - Componente principal
import { useState } from "react";
import { SearchForm } from "@/components/search-form";
import { ChemicalCard } from "@/components/details-card-molecule";

interface DataStructure {
  name: string;
  formula: string;
  molar_mass: number;
}

function Search() {
  const [data, setData] = useState<DataStructure | null>(null);

  return (
    <div className="flex flex-col items-center justify-center">
      <SearchForm onSearch={setData} />
      <ChemicalCard data={data} />
    </div>
  );
}

export default Search;
