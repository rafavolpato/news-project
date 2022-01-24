import { Page } from "./page-model";
export class News extends Page {
  public id!: number;
  public siteName!: string;
  public link!: string;
  public title!: string;
  public summary!: string;
  public tenpo!: number;
  public click_count!: number;

  public constructor (init?: Partial<News>) {
    super(init)
  }
}
