export class Page {
  public count!: number;
  public next!: string;
  public prev!: string;
  public results!: any;

  public constructor (init?: Partial<Page>) {
    Object.assign(this, init)
  }
}
