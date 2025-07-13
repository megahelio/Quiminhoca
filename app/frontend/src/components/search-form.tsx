import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "./ui/form";
import { Input } from "./ui/input";
import { Button } from "./ui/button";

type SearchFormProps = {
  onSearch: (data: {
    name: string;
    formula: string;
    molar_mass: number;
  }) => void;
};

const searchSchema = z.object({
  formula: z.string().min(2, {
    message: "Formula must be at least 2 characters.",
  }),
});

export function SearchForm({ onSearch }: Readonly<SearchFormProps>) {
  // 1. Define your form.
  const form = useForm<z.infer<typeof searchSchema>>({
    resolver: zodResolver(searchSchema),
    defaultValues: {
      formula: "",
    },
  });

  // 2. Define a submit handler.
  function onSubmit(values: z.infer<typeof searchSchema>) {
    // Do something with the form values.
    // ✅ This will be type-safe and validated.

    /*TODO const res = await axios.post('http://localhost:8000/api/parse', {
             notation
         });*/

    console.log(values);
    onSearch({
      name: "2,2′,2″,2′″-(etano-1,2-diil)dinitrilo",
      formula: values.formula,
      molar_mass: 73,
    });
  }

  return (
    <div className="shadow-lgrounded-xl mb-4 flex flex-col items-center justify-center rounded-xl bg-white p-10 shadow-lg">
      <h1 className="text-l font-bold">Search</h1>
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
          <FormField
            control={form.control}
            name="formula"
            render={({ field }) => (
              <FormItem>
                <FormLabel className="mb-2 block text-gray-700 dark:text-white">
                  Fórmula
                </FormLabel>
                <FormControl>
                  <Input placeholder="ej:C6H6" {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <Button type="submit">Consultar</Button>
        </form>
      </Form>
    </div>
  );
}
