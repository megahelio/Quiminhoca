import { Card, CardHeader, CardContent } from "@/components/ui/card";

type ChemicalData = {
  name: string;
  formula: string;
  molar_mass: number;
};

type ChemicalCardProps = {
  data: ChemicalData | null;
};

export function ChemicalCard({ data }: Readonly<ChemicalCardProps>) {
  if (!data) return null;

  return (
    <Card className="mb-4">
      <CardHeader>
        <h2 className="text-xl font-semibold">{data.name}</h2>
        <span className="text-muted-foreground text-sm">{data.formula}</span>
      </CardHeader>
      <CardContent>
        <p className="text-sm">Masa molar: {data.molar_mass} g/mol</p>
      </CardContent>
    </Card>
  );
}
