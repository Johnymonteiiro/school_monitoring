import { SearchForm } from "@/components/search-form";
import { UserPlus, GraduationCap } from "lucide-react";
import { Modal } from "../../../components/modal";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { TableContent } from "@/components/table";
import { DataTableDemo } from "@/components/table_2";

export default function Students() {
  return (
    <div className="flex flex-1 flex-col gap-4 p-4">
      <div className="min-h-[100vh] flex-1 rounded-xl bg-muted/50 md:min-h-min p-4">
        <div className="flex justify-between items-center">
          <div className="flex items-center">
            <GraduationCap className="stroke-blue-500" />
            <strong className="ml-2">Students</strong>
          </div>

          <div className="flex items-center">
            <SearchForm className="px-2" />
            <Modal
              button={{
                icon: UserPlus,
                label: "New Student",
              }}
            >
              <div className="grid gap-4 py-4">
                <div className="grid grid-cols-4 items-center gap-4">
                  <Label htmlFor="name" className="text-right">
                    Name
                  </Label>
                  <Input
                    id="name"
                    defaultValue="Pedro Duarte"
                    className="col-span-3"
                  />
                </div>
                <div className="grid grid-cols-4 items-center gap-4">
                  <Label htmlFor="username" className="text-right">
                    Username
                  </Label>
                  <Input
                    id="username"
                    defaultValue="@peduarte"
                    className="col-span-3"
                  />
                </div>
              </div>
            </Modal>
          </div>
        </div>

        <DataTableDemo />
      </div>
    </div>
  );
}
