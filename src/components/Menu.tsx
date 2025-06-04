import React, { useEffect, useState } from 'react';
import { 
    Grid, 
    Card, 
    CardContent, 
    Typography, 
    CardActions, 
    Button,
    CircularProgress,
    Container
} from '@mui/material';
import { Pizza } from '../types';
import { menuAPI } from '../services/api';

const Menu: React.FC = () => {
    const [pizzas, setPizzas] = useState<Pizza[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchMenu = async () => {
            try {
                const data = await menuAPI.getMenu();
                setPizzas(data);
            } catch (err) {
                setError('Failed to load menu');
                console.error('Error fetching menu:', err);
            } finally {
                setLoading(false);
            }
        };

        fetchMenu();
    }, []);

    if (loading) {
        return (
            <Container sx={{ display: 'flex', justifyContent: 'center', mt: 4 }}>
                <CircularProgress />
            </Container>
        );
    }

    if (error) {
        return (
            <Container>
                <Typography color="error" align="center">
                    {error}
                </Typography>
            </Container>
        );
    }

    return (
        <Container>
            <Typography variant="h4" component="h1" gutterBottom align="center" sx={{ mt: 4 }}>
                Our Pizza Menu
            </Typography>
            <Grid container spacing={3}>
                {pizzas.map((pizza) => (
                    <Grid item xs={12} sm={6} md={4} key={pizza.id}>
                        <Card>
                            <CardContent>
                                <Typography variant="h5" component="h2">
                                    {pizza.name}
                                </Typography>
                                <Typography color="textSecondary" gutterBottom>
                                    Size: {pizza.size}
                                </Typography>
                                <Typography variant="body2" component="p">
                                    Ingredients: {pizza.ingredients.join(', ')}
                                </Typography>
                                <Typography variant="h6" sx={{ mt: 2 }}>
                                    ${pizza.price.toFixed(2)}
                                </Typography>
                            </CardContent>
                            <CardActions>
                                <Button size="small" color="primary">
                                    Add to Order
                                </Button>
                            </CardActions>
                        </Card>
                    </Grid>
                ))}
            </Grid>
        </Container>
    );
};

export default Menu; 