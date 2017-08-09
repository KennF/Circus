import { Component } from '@angular/core';
import { OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Hero } from './hero';
import { HeroService } from './hero.service';

@Component({
  selector: 'my-heroes',
  templateUrl: './heroes.component.html',
  styleUrls: [ './heroes.component.css' ]
})

export class HeroesComponent implements OnInit {
  title = 'Tour of heroes';
  heroes: Hero[];
  selectedHero: Hero;

  constructor(
    private router: Router,
    private heroService: HeroService) { }

  onSelect(hero: Hero): void {
    this.selectedHero = hero;
  };

  ngOnInit(): void {
    this.getHeroes();
  };

  getHeroes(): void {
    this.heroService.getHeroes().then(heros => this.heroes = heros);
  }

  gotoDetail(): void {
    this.router.navigate(['/detail', this.selectedHero.id]);
  }


}
